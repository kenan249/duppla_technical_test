import React from "react";
import { DocumentsTable } from "./DocumentsTable";
import { TablePaginationFooter } from "./TablePaginationFooter";

export function DocumentsTableCard() {
  return (
    <section className="bg-white dark:bg-slate-900 rounded-xl shadow-sm border border-slate-200 dark:border-slate-800 overflow-hidden">
      <div className="overflow-x-auto">
        <DocumentsTable />
      </div>
      <TablePaginationFooter />
    </section>
  );
}