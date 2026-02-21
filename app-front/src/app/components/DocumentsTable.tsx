import React from "react";

export function DocumentsTable() {
  return (
    <table className="w-full text-left border-collapse">
      <thead>
        <tr className="bg-slate-50 dark:bg-slate-800/50 border-b border-slate-200 dark:border-slate-800">
          <th className="py-4 px-6 w-10">
            <input className="rounded border-slate-300 dark:border-slate-700 text-primary focus:ring-primary" type="checkbox" />
          </th>
          <th className="py-4 px-4 text-xs font-bold text-slate-500 uppercase tracking-wider">ID</th>
          <th className="py-4 px-4 text-xs font-bold text-slate-500 uppercase tracking-wider">Type</th>
          <th className="py-4 px-4 text-xs font-bold text-slate-500 uppercase tracking-wider text-right">Amount</th>
          <th className="py-4 px-4 text-xs font-bold text-slate-500 uppercase tracking-wider text-center">Status</th>
          <th className="py-4 px-4 text-xs font-bold text-slate-500 uppercase tracking-wider">Created At</th>
          <th className="py-4 px-4 text-xs font-bold text-slate-500 uppercase tracking-wider text-right">Actions</th>
        </tr>
      </thead>

      <tbody className="divide-y divide-slate-100 dark:divide-slate-800">
        {/* Row 1 */}
        <tr className="hover:bg-slate-50/50 dark:hover:bg-slate-800/30 transition-colors">
          <td className="py-4 px-6">
            <input className="rounded border-slate-300 dark:border-slate-700 text-primary focus:ring-primary" type="checkbox" defaultChecked />
          </td>
          <td className="py-4 px-4">
            <div className="flex items-center gap-2 group cursor-pointer">
              <span className="text-sm font-mono text-slate-600 dark:text-slate-400">DOC-9812</span>
              <span className="material-symbols-outlined text-slate-300 group-hover:text-primary transition-colors text-[16px]">
                content_copy
              </span>
            </div>
          </td>
          <td className="py-4 px-4 text-sm font-medium">Invoice</td>
          <td className="py-4 px-4 text-sm font-bold text-right">$1,240.00</td>
          <td className="py-4 px-4 text-center">
            <span className="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-bold bg-blue-100 text-blue-700 dark:bg-blue-900/30 dark:text-blue-400 uppercase tracking-tighter">
              Pending
            </span>
          </td>
          <td className="py-4 px-4 text-sm text-slate-500">Oct 24, 2023</td>
          <td className="py-4 px-4 text-right space-x-2">
            <button className="p-1.5 text-slate-400 hover:text-primary rounded-md hover:bg-slate-100 dark:hover:bg-slate-800">
              <span className="material-symbols-outlined text-[18px]">edit</span>
            </button>
            <button className="p-1.5 text-slate-400 hover:text-rose-500 rounded-md hover:bg-slate-100 dark:hover:bg-slate-800">
              <span className="material-symbols-outlined text-[18px]">delete</span>
            </button>
          </td>
        </tr>

        {/* Row 2 */}
        <tr className="hover:bg-slate-50/50 dark:hover:bg-slate-800/30 transition-colors">
          <td className="py-4 px-6">
            <input className="rounded border-slate-300 dark:border-slate-700 text-primary focus:ring-primary" type="checkbox" defaultChecked />
          </td>
          <td className="py-4 px-4">
            <div className="flex items-center gap-2 group cursor-pointer">
              <span className="text-sm font-mono text-slate-600 dark:text-slate-400">DOC-1234</span>
              <span className="material-symbols-outlined text-slate-300 group-hover:text-primary transition-colors text-[16px]">
                content_copy
              </span>
            </div>
          </td>
          <td className="py-4 px-4 text-sm font-medium">Receipt</td>
          <td className="py-4 px-4 text-sm font-bold text-right">$85.20</td>
          <td className="py-4 px-4 text-center">
            <span className="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-bold bg-emerald-100 text-emerald-700 dark:bg-emerald-900/30 dark:text-emerald-400 uppercase tracking-tighter">
              Approved
            </span>
          </td>
          <td className="py-4 px-4 text-sm text-slate-500">Oct 23, 2023</td>
          <td className="py-4 px-4 text-right space-x-2">
            <button className="p-1.5 text-slate-400 hover:text-primary rounded-md hover:bg-slate-100 dark:hover:bg-slate-800">
              <span className="material-symbols-outlined text-[18px]">edit</span>
            </button>
            <button className="p-1.5 text-slate-400 hover:text-rose-500 rounded-md hover:bg-slate-100 dark:hover:bg-slate-800">
              <span className="material-symbols-outlined text-[18px]">delete</span>
            </button>
          </td>
        </tr>

        {/* Row 3 */}
        <tr className="hover:bg-slate-50/50 dark:hover:bg-slate-800/30 transition-colors">
          <td className="py-4 px-6">
            <input className="rounded border-slate-300 dark:border-slate-700 text-primary focus:ring-primary" type="checkbox" />
          </td>
          <td className="py-4 px-4">
            <div className="flex items-center gap-2 group cursor-pointer">
              <span className="text-sm font-mono text-slate-600 dark:text-slate-400">DOC-5561</span>
              <span className="material-symbols-outlined text-slate-300 group-hover:text-primary transition-colors text-[16px]">
                content_copy
              </span>
            </div>
          </td>
          <td className="py-4 px-4 text-sm font-medium">Contract</td>
          <td className="py-4 px-4 text-sm font-bold text-right">$0.00</td>
          <td className="py-4 px-4 text-center">
            <span className="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-bold bg-slate-100 text-slate-600 dark:bg-slate-800 dark:text-slate-400 uppercase tracking-tighter">
              Draft
            </span>
          </td>
          <td className="py-4 px-4 text-sm text-slate-500">Oct 22, 2023</td>
          <td className="py-4 px-4 text-right space-x-2">
            <button className="p-1.5 text-slate-400 hover:text-primary rounded-md hover:bg-slate-100 dark:hover:bg-slate-800">
              <span className="material-symbols-outlined text-[18px]">edit</span>
            </button>
            <button className="p-1.5 text-slate-400 hover:text-rose-500 rounded-md hover:bg-slate-100 dark:hover:bg-slate-800">
              <span className="material-symbols-outlined text-[18px]">delete</span>
            </button>
          </td>
        </tr>

        {/* Row 4 */}
        <tr className="hover:bg-slate-50/50 dark:hover:bg-slate-800/30 transition-colors">
          <td className="py-4 px-6">
            <input className="rounded border-slate-300 dark:border-slate-700 text-primary focus:ring-primary" type="checkbox" defaultChecked />
          </td>
          <td className="py-4 px-4">
            <div className="flex items-center gap-2 group cursor-pointer">
              <span className="text-sm font-mono text-slate-600 dark:text-slate-400">DOC-4432</span>
              <span className="material-symbols-outlined text-slate-300 group-hover:text-primary transition-colors text-[16px]">
                content_copy
              </span>
            </div>
          </td>
          <td className="py-4 px-4 text-sm font-medium">Invoice</td>
          <td className="py-4 px-4 text-sm font-bold text-right">$4,500.00</td>
          <td className="py-4 px-4 text-center">
            <span className="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-bold bg-rose-100 text-rose-700 dark:bg-rose-900/30 dark:text-rose-400 uppercase tracking-tighter">
              Rejected
            </span>
          </td>
          <td className="py-4 px-4 text-sm text-slate-500">Oct 21, 2023</td>
          <td className="py-4 px-4 text-right space-x-2">
            <button className="p-1.5 text-slate-400 hover:text-primary rounded-md hover:bg-slate-100 dark:hover:bg-slate-800">
              <span className="material-symbols-outlined text-[18px]">edit</span>
            </button>
            <button className="p-1.5 text-slate-400 hover:text-rose-500 rounded-md hover:bg-slate-100 dark:hover:bg-slate-800">
              <span className="material-symbols-outlined text-[18px]">delete</span>
            </button>
          </td>
        </tr>
      </tbody>
    </table>
  );
}