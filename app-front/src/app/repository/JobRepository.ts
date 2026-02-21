
const basePath = 'ws://localhost:8000';
export const connectJobWs = (onMessage: (data: any) => void, onError: (error: any) => void): WebSocket => {
    const ws = new WebSocket(`${basePath}/jobs/ws`);
    
    ws.onmessage = (event) => {
        const data = JSON.parse(event.data);
        onMessage(data);
    };

    ws.onerror = (error) => {
        onError(error);
    };

    return ws;
}