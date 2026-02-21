import React from "react";

export function JobProgressCard() {
  return (
    <section className="bg-white dark:bg-slate-900 rounded-xl shadow-sm border border-slate-200 dark:border-slate-800 p-6">
      <div className="flex items-center justify-between mb-4">
        <div className="flex items-center gap-2">
          <span className="material-symbols-outlined text-primary">task</span>
          <h3 className="text-lg font-bold text-slate-900 dark:text-white">Active Job</h3>
        </div>
        <span className="inline-flex items-center px-2 py-0.5 rounded text-[10px] font-black bg-primary/10 text-primary uppercase animate-pulse">
          Running
        </span>
      </div>

      <div className="space-y-4">
        <div className="flex justify-between text-xs font-medium">
          <span className="text-slate-400 font-mono">ID: JOB-00421</span>
          <span className="text-primary font-bold">65%</span>
        </div>

        <div className="h-2.5 w-full bg-slate-100 dark:bg-slate-800 rounded-full overflow-hidden">
          <div className="h-full bg-primary rounded-full transition-all duration-500" style={{ width: "65%" }} />
        </div>

        <div className="bg-slate-50 dark:bg-slate-800/50 p-3 rounded-lg border border-slate-100 dark:border-slate-800">
          <p className="text-[11px] font-bold text-slate-400 uppercase mb-1">Current Item</p>
          <p className="text-sm font-semibold text-slate-700 dark:text-slate-300 flex items-center gap-2">
            <span className="w-1.5 h-1.5 rounded-full bg-primary" />
            Processing: DOC-1234
          </p>
        </div>

        <div className="grid grid-cols-2 gap-3 pt-2">
          <div className="text-center p-2 rounded-lg bg-emerald-50 dark:bg-emerald-900/20 border border-emerald-100 dark:border-emerald-900/40">
            <p className="text-[10px] font-bold text-emerald-600 dark:text-emerald-400 uppercase">Success</p>
            <p className="text-lg font-black text-emerald-700 dark:text-emerald-400">32</p>
          </div>

          <div className="text-center p-2 rounded-lg bg-rose-50 dark:bg-rose-900/20 border border-rose-100 dark:border-rose-900/40">
            <p className="text-[10px] font-bold text-rose-600 dark:text-rose-400 uppercase">Failed</p>
            <p className="text-lg font-black text-rose-700 dark:text-rose-400">1</p>
          </div>
        </div>
      </div>
    </section>
  );
}