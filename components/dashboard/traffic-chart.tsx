"use client"

import {
  Line,
  LineChart,
  XAxis,
  YAxis,
  CartesianGrid,
  ResponsiveContainer,
} from "recharts"
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { ChartContainer, ChartTooltip, ChartTooltipContent } from "@/components/ui/chart"
import { ArrowRight } from "lucide-react"
import { Button } from "@/components/ui/button"

const trafficData = [
  { time: "12h ago", incoming: 1200, outgoing: 800 },
  { time: "10h ago", incoming: 1400, outgoing: 920 },
  { time: "8h ago", incoming: 1800, outgoing: 1100 },
  { time: "6h ago", incoming: 2200, outgoing: 1400 },
  { time: "4h ago", incoming: 1900, outgoing: 1200 },
  { time: "2h ago", incoming: 2400, outgoing: 1600 },
  { time: "Now", incoming: 2100, outgoing: 1300 },
]

const chartConfig = {
  incoming: {
    label: "Incoming",
    color: "hsl(160, 65%, 50%)",
  },
  outgoing: {
    label: "Outgoing",
    color: "hsl(220, 70%, 55%)",
  },
}

export function TrafficChart() {
  return (
    <Card className="bg-card">
      <CardHeader className="flex flex-row items-center justify-between">
        <div>
          <CardTitle className="text-base font-medium">Data Transfer</CardTitle>
          <div className="mt-2 flex items-center gap-4">
            <div className="flex items-center gap-2">
              <div className="h-2 w-2 rounded-full bg-emerald-500" />
              <span className="text-sm text-muted-foreground">Incoming</span>
              <span className="font-semibold text-foreground">102GB</span>
            </div>
            <div className="flex items-center gap-2">
              <div className="h-2 w-2 rounded-full bg-blue-500" />
              <span className="text-sm text-muted-foreground">Outgoing</span>
              <span className="font-semibold text-foreground">496GB</span>
            </div>
          </div>
        </div>
        <Button variant="ghost" size="sm" className="gap-1 text-muted-foreground">
          View Details
          <ArrowRight className="h-3 w-3" />
        </Button>
      </CardHeader>
      <CardContent>
        <ChartContainer config={chartConfig} className="h-[280px] w-full">
          <ResponsiveContainer width="100%" height="100%">
            <LineChart data={trafficData} margin={{ top: 10, right: 10, left: 0, bottom: 0 }}>
              <CartesianGrid strokeDasharray="3 3" stroke="hsl(240, 5%, 18%)" />
              <XAxis
                dataKey="time"
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
                tickFormatter={(value) => `${value}MB`}
              />
              <ChartTooltip content={<ChartTooltipContent />} />
              <Line
                type="monotone"
                dataKey="incoming"
                stroke="hsl(160, 65%, 50%)"
                strokeWidth={2}
                dot={false}
              />
              <Line
                type="monotone"
                dataKey="outgoing"
                stroke="hsl(220, 70%, 55%)"
                strokeWidth={2}
                dot={false}
              />
            </LineChart>
          </ResponsiveContainer>
        </ChartContainer>
      </CardContent>
    </Card>
  )
}
