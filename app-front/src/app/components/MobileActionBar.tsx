import React from "react";

export function MobileActionBar() {
  return (
    <div className="fixed bottom-6 left-1/2 -translate-x-1/2 bg-slate-900 text-white px-6 py-3 rounded-full shadow-2xl flex items-center gap-6 md:hidden z-50">
      <span className="text-sm font-bold">5 selected</span>
      <div className="w-px h-4 bg-slate-700" />
      <button className="text-sm font-bold text-primary">Quick Process</button>
    </div>
  );
}