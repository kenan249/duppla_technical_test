import React from "react";
import { TopNavBar } from "./app/components/TopNavBar";
import { DashboardHeader } from "./app/components/DashboardHeader";
import { FiltersCard } from "./app/components/FiltersCard";
import { DocumentsTableCard } from "./app/components/DocumentsTableCard";
import { BatchProcessingCard } from "./app/components/BatchProcessingCard";
import { JobProgressCard } from "./app/components/JobProgressCard";
import { ProTipCard } from "./app/components/ProTipCard";
import { MobileActionBar } from "./app/components/MobileActionBar";

export function App() {
  return (
    <div className="bg-background-light dark:bg-background-dark text-slate-900 dark:text-slate-100 min-h-screen">
      <TopNavBar />

      <main className="max-w-7xl mx-auto px-6 lg:px-12 py-8">
        <DashboardHeader />

        <div className="grid grid-cols-1 lg:grid-cols-[1fr_320px] gap-8">
          {/* Left Column */}
          <div className="space-y-6">
            <FiltersCard />
            <DocumentsTableCard />
          </div>

          {/* Right Column */}
          <aside className="space-y-6">
            <BatchProcessingCard />
            <JobProgressCard />
            <ProTipCard />
          </aside>
        </div>
      </main>

      <MobileActionBar />
    </div>
  );
}