export interface JobEvent {
  status: string;
  processed: number;
  total: number;
  target_status: string;
  current_document_id?: string;
  result?: string;
  reason?: string;
  succeeded?: number;
  failed?: number;
  error?: string;
  message?: string;
}
export const JobStatus = {
    PENDING: 'pending',
    IN_PROGRESS: 'in_progress',
    COMPLETED: 'completed',
    FAILED: 'failed',
} as const;

export type JobStatus = typeof JobStatus[keyof typeof JobStatus];

export interface Job {
    id: string;
    status: JobStatus;
    created_at: string;
    updated_at: string;
    error_message?: string;
}