"use client"

import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { TrendingUp, TrendingDown, Minus } from "lucide-react"

const departments = [
  { name: "Electrical Engineering", positions: 254, trend: "up", change: "+12%" },
  { name: "Mechanical Engineering", positions: 252, trend: "up", change: "+8%" },
  { name: "Computer Science", positions: 185, trend: "up", change: "+15%" },
  { name: "Information Engineering", positions: 172, trend: "neutral", change: "0%" },
  { name: "Civil Engineering", positions: 163, trend: "down", change: "-3%" },
  { name: "Environmental Science", positions: 154, trend: "up", change: "+5%" },
]

export function TopDepartments() {
  return (
    <Card className="bg-card">
      <CardHeader className="pb-2">
        <CardTitle className="text-base font-medium">
          Department Rankings
        </CardTitle>
        <p className="text-sm text-muted-foreground">
          Hiring trends by department
        </p>
      </CardHeader>
      <CardContent>
        <div className="space-y-3">
          {departments.map((dept, index) => (
            <div
              key={dept.name}
              className="flex items-center justify-between rounded-lg bg-secondary/50 px-3 py-2"
            >
              <div className="flex items-center gap-3">
                <span className="flex h-6 w-6 items-center justify-center rounded-full bg-primary/10 text-xs font-medium text-primary">
                  {index + 1}
                </span>
                <div>
                  <p className="text-sm font-medium text-foreground">{dept.name}</p>
                  <p className="text-xs text-muted-foreground">{dept.positions} positions</p>
                </div>
              </div>
              <div className="flex items-center gap-1">
                {dept.trend === "up" && (
                  <TrendingUp className="h-3 w-3 text-emerald-500" />
                )}
                {dept.trend === "down" && (
                  <TrendingDown className="h-3 w-3 text-red-500" />
                )}
                {dept.trend === "neutral" && (
                  <Minus className="h-3 w-3 text-muted-foreground" />
                )}
                <span
                  className={`text-xs ${
                    dept.trend === "up"
                      ? "text-emerald-500"
                      : dept.trend === "down"
                      ? "text-red-500"
                      : "text-muted-foreground"
                  }`}
                >
                  {dept.change}
                </span>
              </div>
            </div>
          ))}
        </div>
      </CardContent>
    </Card>
  )
}
