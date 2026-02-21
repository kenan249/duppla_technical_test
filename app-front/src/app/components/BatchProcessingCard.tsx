import React from "react";

export function BatchProcessingCard() {
  return (
    <section className="bg-white dark:bg-slate-900 rounded-xl shadow-sm border border-slate-200 dark:border-slate-800 p-6">
      <div className="flex items-center gap-2 mb-4">
        <span className="material-symbols-outlined text-primary">dynamic_feed</span>
        <h3 className="text-lg font-bold text-slate-900 dark:text-white">Batch Processing</h3>
      </div>

      <p className="text-sm text-slate-500 dark:text-slate-400 mb-6 leading-relaxed">
        Select multiple documents from the list to update their status or export them in bulk.
      </p>

      <div className="space-y-4">
        <div className="flex flex-col gap-1.5">
          <label className="text-xs font-bold text-slate-500 uppercase tracking-wider">Target Status</label>
          <select className="w-full bg-slate-50 dark:bg-slate-800 border-slate-200 dark:border-slate-700 rounded-lg text-sm focus:ring-primary focus:border-primary">
            <option>Approved</option>
            <option>Rejected</option>
            <option>Pending Review</option>
          </select>
        </div>

        <button className="w-full py-3 bg-primary text-white font-bold rounded-lg shadow-lg shadow-primary/30 hover:bg-primary/90 transition-all flex items-center justify-center gap-2 active:scale-[0.98]">
          <span className="material-symbols-outlined text-[20px]">play_arrow</span>
          Process Selected
        </button>
      </div>
    </section>
  );
}