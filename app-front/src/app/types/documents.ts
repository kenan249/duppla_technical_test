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
