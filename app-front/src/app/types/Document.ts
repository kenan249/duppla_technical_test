export const DocumentStatus = {
	DRAFT: 'draft',
	PENDING: 'pending',
	APPROVED: 'approved',
	REJECTED: 'rejected',
} as const;

export type DocumentStatus = typeof DocumentStatus[keyof typeof DocumentStatus];

export interface Document {
	id: string;
	type: string;
	amount: number;
	status: DocumentStatus;
	created_at: string;
	metadata?: Record<string, any>;
}

export interface DocumentFilters {
	page: number;
	page_size: number;
	document_type?: string;
	status?: DocumentStatus;
}

export interface DocumentPage {
	items: Document[];
	total: number;
	page: number;
	page_size: number;
}

export interface CreateDocumentRequest {
	type: string;
	amount: number;
	metadata?: Record<string, any>;
}