import React from "react";

export function TopNavBar() {
  return (
    <header className="sticky top-0 z-50 bg-white dark:bg-slate-900 border-b border-slate-200 dark:border-slate-800 px-6 lg:px-12 py-3">
      <div className="max-w-7xl mx-auto flex items-center justify-between">
        <div className="flex items-center gap-8">
          <div className="flex items-center gap-3">
            <div className="bg-primary text-white p-1.5 rounded-lg flex items-center justify-center">
              <span className="material-symbols-outlined text-xl">description</span>
            </div>
            <h2 className="text-slate-900 dark:text-white text-xl font-bold tracking-tight">
              DocProcessor
            </h2>
          </div>

          <nav className="hidden md:flex items-center gap-8">
            <a className="text-primary text-sm font-semibold border-b-2 border-primary py-4 -mb-4" href="#">
              Documents
            </a>
            <a className="text-slate-500 dark:text-slate-400 hover:text-primary transition-colors text-sm font-medium" href="#">
              Reports
            </a>
            <a className="text-slate-500 dark:text-slate-400 hover:text-primary transition-colors text-sm font-medium" href="#">
              Settings
            </a>
          </nav>
        </div>

        <div className="flex items-center gap-4">
          <div className="relative hidden sm:block">
            <span className="material-symbols-outlined absolute left-3 top-1/2 -translate-y-1/2 text-slate-400 text-lg">
              search
            </span>
            <input
              className="bg-slate-100 dark:bg-slate-800 border-none rounded-lg pl-10 pr-4 py-2 text-sm focus:ring-2 focus:ring-primary w-64"
              placeholder="Search files..."
              type="text"
            />
          </div>

          <button className="p-2 text-slate-500 hover:bg-slate-100 dark:hover:bg-slate-800 rounded-lg">
            <span className="material-symbols-outlined">notifications</span>
          </button>

          <button className="p-2 text-slate-500 hover:bg-slate-100 dark:hover:bg-slate-800 rounded-lg">
            <span className="material-symbols-outlined">account_circle</span>
          </button>
        </div>
      </div>
    </header>
  );
}