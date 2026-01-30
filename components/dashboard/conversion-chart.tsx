"use client"

import {
  Bar,
  BarChart,
  XAxis,
  YAxis,
  ResponsiveContainer,
} from "recharts"
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { ChartContainer, ChartTooltip, ChartTooltipContent } from "@/components/ui/chart"
import { ArrowRight } from "lucide-react"
import { Button } from "@/components/ui/button"

const conversionData = [
  { hour: "00", error: 0.1, timeout: 0.05 },
  { hour: "04", error: 0.2, timeout: 0.08 },
  { hour: "08", error: 0.15, timeout: 0.1 },
  { hour: "12", error: 0.3, timeout: 0.12 },
  { hour: "16", error: 0.25, timeout: 0.1 },
  { hour: "20", error: 0.18, timeout: 0.06 },
]

const chartConfig = {
  error: {
    label: "Error Rate",
    color: "hsl(0, 70%, 55%)",
  },
  timeout: {
    label: "Timeout",
    color: "hsl(35, 85%, 55%)",
  },
}

export function ConversionChart() {
  return (
    <Card className="bg-card">
      <CardHeader className="flex flex-row items-center justify-between pb-2">
        <div>
          <CardTitle className="text-base font-medium">Error Rates</CardTitle>
          <div className="mt-2 flex items-center gap-4">
            <div className="flex items-center gap-2">
              <div className="h-2 w-2 rounded-full bg-red-500" />
              <span className="text-sm text-muted-foreground">Error</span>
              <span className="font-semibold text-foreground">0.2%</span>
            </div>
            <div className="flex items-center gap-2">
              <div className="h-2 w-2 rounded-full bg-amber-500" />
              <span className="text-sm text-muted-foreground">Timeout</span>
              <span className="font-semibold text-foreground">{"<0.1%"}</span>
            </div>
          </div>
        </div>
        <Button variant="ghost" size="icon" className="h-8 w-8">
          <ArrowRight className="h-4 w-4" />
        </Button>
      </CardHeader>
      <CardContent>
        <ChartContainer config={chartConfig} className="h-[200px] w-full">
          <ResponsiveContainer width="100%" height="100%">
            <BarChart data={conversionData} margin={{ top: 10, right: 10, left: 0, bottom: 0 }}>
              <XAxis
                dataKey="hour"
                stroke="hsl(240, 5%, 55%)"
                fontSize={12}
                tickLine={false}
                axisLine={false}
              />
              <YAxis
                stroke="hsl(240, 5%, 55%)"
                fontSize={12}
                tickLine={false}
                axisLine={false}
                tickFormatter={(value) => `${value}%`}
              />
              <ChartTooltip content={<ChartTooltipContent />} />
              <Bar dataKey="error" fill="hsl(0, 70%, 55%)" radius={[2, 2, 0, 0]} />
              <Bar dataKey="timeout" fill="hsl(35, 85%, 55%)" radius={[2, 2, 0, 0]} />
            </BarChart>
          </ResponsiveContainer>
        </ChartContainer>
      </CardContent>
    </Card>
  )
}
