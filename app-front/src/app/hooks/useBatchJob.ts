import { useState, useRef, useEffect } from "react";
import axios from "axios";
import {type JobEvent } from "../types/Job";

export function useBatchJob() {
  const [jobId, setJobId] = useState<string | null>(null);
  const [event, setEvent] = useState<JobEvent | null>(null);
  const [isRunning, setIsRunning] = useState(false);
  const wsRef = useRef<WebSocket | null>(null);

  const start = async (document_ids: string[], target_status: string) => {
    setIsRunning(true);
    const { data } = await axios.post("/documents/batch/process", {
      document_ids,
      target_status,
    });
    setJobId(data.job_id);

    const ws = new WebSocket(`${import.meta.env.VITE_APP_WS_BASE_URL}/ws/jobs/${data.job_id}`);
    ws.onmessage = (msg) => {
      const jobEvent: JobEvent = JSON.parse(msg.data);
      setEvent(jobEvent);
      if (jobEvent.status === "completed" || jobEvent.status === "failed") {
        setIsRunning(false);
        ws.close();
      }
    };
    wsRef.current = ws;
  };

  const reset = () => {
    setJobId(null);
    setEvent(null);
    setIsRunning(false);
    wsRef.current?.close();
    wsRef.current = null;
  };

  useEffect(() => {
    return () => {
      wsRef.current?.close();
    };
  }, []);

  return {
    jobId,
    event,
    isRunning,
    start,
    reset,
  };
}
