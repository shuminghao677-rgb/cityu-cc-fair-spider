"use client"

import { Building2, GraduationCap, Code2, Briefcase } from "lucide-react"
import { Card, CardContent } from "@/components/ui/card"

const kpis = [
  {
    title: "Total Departments",
    value: "32",
    description: "Engineering & Science fields",
    icon: Building2,
    color: "text-blue-500",
    bgColor: "bg-blue-500/10",
  },
  {
    title: "Education Levels",
    value: "3",
    description: "Bachelor, Master, Doctoral",
    icon: GraduationCap,
    color: "text-emerald-500",
    bgColor: "bg-emerald-500/10",
  },
  {
    title: "Technical Skills",
    value: "30",
    description: "In-demand skills tracked",
    icon: Code2,
    color: "text-amber-500",
    bgColor: "bg-amber-500/10",
  },
  {
    title: "Total Positions",
    value: "4,500+",
    description: "Job openings analyzed",
    icon: Briefcase,
    color: "text-purple-500",
    bgColor: "bg-purple-500/10",
  },
]

export function KPICards() {
  return (
    <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
      {kpis.map((kpi) => (
        <Card key={kpi.title} className="bg-card">
          <CardContent className="p-6">
            <div className="flex items-center justify-between">
              <div className={`flex h-10 w-10 items-center justify-center rounded-lg ${kpi.bgColor}`}>
                <kpi.icon className={`h-5 w-5 ${kpi.color}`} />
              </div>
            </div>
            <div className="mt-4">
              <p className="text-3xl font-bold text-foreground">{kpi.value}</p>
              <p className="text-sm font-medium text-foreground">{kpi.title}</p>
            </div>
            <p className="mt-2 text-xs text-muted-foreground">{kpi.description}</p>
          </CardContent>
        </Card>
      ))}
    </div>
  )
}
