import React from "react";

export function ProTipCard() {
  return (
    <div className="bg-primary/5 rounded-xl p-6 border border-primary/10">
      <div className="flex gap-3">
        <span className="material-symbols-outlined text-primary">info</span>
        <div>
          <p className="text-sm font-bold text-slate-900 dark:text-white mb-1">Pro Tip</p>
          <p className="text-xs text-slate-500 dark:text-slate-400 leading-relaxed">
            Use{" "}
            <kbd className="px-1.5 py-0.5 rounded bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 font-mono">
              Shift + Click
            </kbd>{" "}
            to select multiple documents faster in the table.
          </p>
        </div>
      </div>
    </div>
  );
}