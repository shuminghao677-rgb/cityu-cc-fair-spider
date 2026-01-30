"use client"

import { TrendingUp, TrendingDown, DollarSign, Users, ShoppingCart, Eye } from "lucide-react"
import { Card, CardContent } from "@/components/ui/card"
import { cn } from "@/lib/utils"

const kpis = [
  {
    title: "Total Revenue",
    value: "$128,430",
    change: "+12.5%",
    trend: "up",
    icon: DollarSign,
    description: "vs last period",
  },
  {
    title: "Active Users",
    value: "24,521",
    change: "+8.2%",
    trend: "up",
    icon: Users,
    description: "vs last period",
  },
  {
    title: "Orders",
    value: "1,429",
    change: "-3.1%",
    trend: "down",
    icon: ShoppingCart,
    description: "vs last period",
  },
  {
    title: "Page Views",
    value: "289K",
    change: "+18.7%",
    trend: "up",
    icon: Eye,
    description: "vs last period",
  },
]

export function KPICards() {
  return (
    <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
      {kpis.map((kpi) => (
        <Card key={kpi.title} className="bg-card">
          <CardContent className="p-6">
            <div className="flex items-center justify-between">
              <div className="flex h-10 w-10 items-center justify-center rounded-lg bg-secondary">
                <kpi.icon className="h-5 w-5 text-primary" />
              </div>
              <div
                className={cn(
                  "flex items-center gap-1 text-sm font-medium",
                  kpi.trend === "up" ? "text-emerald-500" : "text-red-500"
                )}
              >
                {kpi.trend === "up" ? (
                  <TrendingUp className="h-4 w-4" />
                ) : (
                  <TrendingDown className="h-4 w-4" />
                )}
                {kpi.change}
              </div>
            </div>
            <div className="mt-4">
              <p className="text-2xl font-bold text-foreground">{kpi.value}</p>
              <p className="text-sm text-muted-foreground">{kpi.title}</p>
            </div>
            <p className="mt-2 text-xs text-muted-foreground">{kpi.description}</p>
          </CardContent>
        </Card>
      ))}
    </div>
  )
}
