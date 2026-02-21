import React from "react";

export function TablePaginationFooter() {
  return (
    <div className="p-4 bg-slate-50 dark:bg-slate-800/50 border-t border-slate-200 dark:border-slate-800 flex flex-col sm:flex-row items-center justify-between gap-4">
      <div className="flex items-center gap-4">
        <span className="bg-primary/10 text-primary px-3 py-1 rounded-full text-xs font-bold border border-primary/20">
          5 selected
        </span>
        <div className="flex items-center gap-2">
          <span className="text-sm text-slate-500">Show</span>
          <select className="bg-white dark:bg-slate-700 border-slate-200 dark:border-slate-600 rounded-lg text-xs py-1">
            <option>15</option>
            <option>30</option>
            <option>50</option>
          </select>
        </div>
      </div>

      <div className="flex items-center gap-2">
        <button
          className="flex items-center gap-1 px-3 py-1.5 rounded-lg border border-slate-200 dark:border-slate-700 text-sm font-medium hover:bg-white dark:hover:bg-slate-700 disabled:opacity-50"
          disabled
        >
          <span className="material-symbols-outlined text-lg">chevron_left</span>
          Prev
        </button>

        <div className="flex items-center gap-1">
          <button className="w-8 h-8 rounded-lg bg-primary text-white text-sm font-bold">1</button>
          <button className="w-8 h-8 rounded-lg text-sm font-bold text-slate-500 hover:bg-slate-100 dark:hover:bg-slate-800">
            2
          </button>
          <button className="w-8 h-8 rounded-lg text-sm font-bold text-slate-500 hover:bg-slate-100 dark:hover:bg-slate-800">
            3
          </button>
        </div>

        <button className="flex items-center gap-1 px-3 py-1.5 rounded-lg border border-slate-200 dark:border-slate-700 text-sm font-medium hover:bg-white dark:hover:bg-slate-700">
          Next
          <span className="material-symbols-outlined text-lg">chevron_right</span>
        </button>
      </div>
    </div>
  );
}