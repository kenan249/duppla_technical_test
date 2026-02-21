import React from "react";

export function DashboardHeader() {
  return (
    <div className="flex flex-col md:flex-row md:items-center justify-between mb-8 gap-4">
      <div>
        <h1 className="text-3xl font-black text-slate-900 dark:text-white tracking-tight">
          Documents
        </h1>
        <p className="text-slate-500 dark:text-slate-400 mt-1">
          Manage, filter and batch process documents
        </p>
      </div>

      <div className="flex items-center gap-3">
        <div className="flex items-center gap-2 bg-primary/10 text-primary px-3 py-1.5 rounded-full text-sm font-semibold border border-primary/20">
          <span className="material-symbols-outlined text-[18px]">check_circle</span>
          API Connected
        </div>

        <button className="flex items-center gap-2 bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 px-4 py-2 rounded-lg text-sm font-bold hover:bg-slate-50 dark:hover:bg-slate-700 transition-colors">
          <span className="material-symbols-outlined text-[18px]">refresh</span>
          Refresh
        </button>
      </div>
    </div>
  );
}