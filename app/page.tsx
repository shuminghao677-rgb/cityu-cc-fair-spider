"use client"

import { Sidebar } from "@/components/dashboard/sidebar"
import { Header } from "@/components/dashboard/header"
import { KPICards } from "@/components/dashboard/kpi-cards"
import { DepartmentChart } from "@/components/dashboard/department-chart"
import { EducationChart } from "@/components/dashboard/education-chart"
import { SkillsChart } from "@/components/dashboard/skills-chart"
import { TopDepartments } from "@/components/dashboard/top-departments"
import { SkillsHeatmap } from "@/components/dashboard/skills-heatmap"

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
              <DepartmentChart />
              <EducationChart />
            </div>
            <div className="grid gap-6 lg:grid-cols-3">
              <SkillsChart />
              <TopDepartments />
              <SkillsHeatmap />
            </div>
          </div>
        </main>
      </div>
    </div>
  )
}
