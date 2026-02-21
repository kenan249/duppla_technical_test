import ProxyClient from "./ProxyClient";
import { type CreateDocumentRequest, type DocumentFilters, type DocumentPage,  }  from "../types/Document";

export const listDocuments = async (params: DocumentFilters): Promise<DocumentPage> => {
    const response = await ProxyClient.get('/documents', { params });
    return response.data;
}

export const createDocument = async (data: CreateDocumentRequest): Promise<Document> => {
    const response = await ProxyClient.post('/documents', data);
    return response.data;
}

export const updateDocument = async (id: string, data: Partial<CreateDocumentRequest>): Promise<Document> => {
    const response = await ProxyClient.patch(`/documents/${id}`, data);
    return response.data;
}

export const deleteDocument = async (id: string): Promise<void> => {
    await ProxyClient.delete(`/documents/${id}`);
}