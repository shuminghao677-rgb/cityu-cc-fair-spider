"use client"

import { Sidebar } from "@/components/dashboard/sidebar"
import { Header } from "@/components/dashboard/header"
import { KPICards } from "@/components/dashboard/kpi-cards"
import { RevenueChart } from "@/components/dashboard/revenue-chart"
import { TrafficChart } from "@/components/dashboard/traffic-chart"
import { ConversionChart } from "@/components/dashboard/conversion-chart"
import { RecentActivity } from "@/components/dashboard/recent-activity"
import { TopProducts } from "@/components/dashboard/top-products"

export default function DashboardPage() {
  return (
    <div className="flex h-screen bg-background">
      <Sidebar />
      <div className="flex flex-1 flex-col overflow-hidden">
        <Header />
        <main className="flex-1 overflow-y-auto p-6">
          <div className="mx-auto max-w-7xl space-y-6">
            <KPICards />
            <div className="grid gap-6 lg:grid-cols-2">
              <RevenueChart />
              <TrafficChart />
            </div>
            <div className="grid gap-6 lg:grid-cols-3">
              <ConversionChart />
              <TopProducts />
              <RecentActivity />
            </div>
          </div>
        </main>
      </div>
    </div>
  )
}
