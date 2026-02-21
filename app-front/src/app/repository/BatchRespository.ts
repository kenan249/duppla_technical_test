import ProxyClient from "./ProxyClient";

const basePath = '/documents/batch';

export const processBatch = async (documents_id: string[], status_target: string): Promise<void> => {
    let request={
        "doucments_id": documents_id,
        "status_target": status_target
    }
    await ProxyClient.post(`${basePath}/process`, request);
}