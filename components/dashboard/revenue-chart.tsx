"use client"

import {
  Area,
  AreaChart,
  XAxis,
  YAxis,
  CartesianGrid,
  ResponsiveContainer,
  Tooltip,
} from "recharts"
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { ChartContainer, ChartTooltip, ChartTooltipContent } from "@/components/ui/chart"
import { ArrowRight } from "lucide-react"
import { Button } from "@/components/ui/button"

const revenueData = [
  { time: "00:00", revenue: 2400, orders: 1200 },
  { time: "02:00", revenue: 1398, orders: 800 },
  { time: "04:00", revenue: 3800, orders: 1600 },
  { time: "06:00", revenue: 3908, orders: 1800 },
  { time: "08:00", revenue: 4800, orders: 2200 },
  { time: "10:00", revenue: 3800, orders: 1900 },
  { time: "12:00", revenue: 4300, orders: 2100 },
  { time: "14:00", revenue: 5300, orders: 2400 },
  { time: "16:00", revenue: 4890, orders: 2200 },
  { time: "18:00", revenue: 5400, orders: 2600 },
  { time: "20:00", revenue: 4200, orders: 2000 },
  { time: "22:00", revenue: 3100, orders: 1500 },
]

const chartConfig = {
  revenue: {
    label: "Revenue",
    color: "hsl(220, 70%, 55%)",
  },
  orders: {
    label: "Orders",
    color: "hsl(35, 85%, 55%)",
  },
}

export function RevenueChart() {
  return (
    <Card className="bg-card">
      <CardHeader className="flex flex-row items-center justify-between">
        <div>
          <CardTitle className="text-base font-medium">Revenue Overview</CardTitle>
          <div className="mt-2 flex items-center gap-4">
            <div className="flex items-center gap-2">
              <div className="h-2 w-2 rounded-full bg-blue-500" />
              <span className="text-sm text-muted-foreground">Revenue</span>
            </div>
            <div className="flex items-center gap-2">
              <div className="h-2 w-2 rounded-full bg-amber-500" />
              <span className="text-sm text-muted-foreground">Orders</span>
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
            <AreaChart data={revenueData} margin={{ top: 10, right: 10, left: 0, bottom: 0 }}>
              <defs>
                <linearGradient id="colorRevenue" x1="0" y1="0" x2="0" y2="1">
                  <stop offset="5%" stopColor="hsl(220, 70%, 55%)" stopOpacity={0.3} />
                  <stop offset="95%" stopColor="hsl(220, 70%, 55%)" stopOpacity={0} />
                </linearGradient>
                <linearGradient id="colorOrders" x1="0" y1="0" x2="0" y2="1">
                  <stop offset="5%" stopColor="hsl(35, 85%, 55%)" stopOpacity={0.3} />
                  <stop offset="95%" stopColor="hsl(35, 85%, 55%)" stopOpacity={0} />
                </linearGradient>
              </defs>
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
                tickFormatter={(value) => `$${value}`}
              />
              <ChartTooltip content={<ChartTooltipContent />} />
              <Area
                type="monotone"
                dataKey="revenue"
                stroke="hsl(220, 70%, 55%)"
                fill="url(#colorRevenue)"
                strokeWidth={2}
              />
              <Area
                type="monotone"
                dataKey="orders"
                stroke="hsl(35, 85%, 55%)"
                fill="url(#colorOrders)"
                strokeWidth={2}
              />
            </AreaChart>
          </ResponsiveContainer>
        </ChartContainer>
      </CardContent>
    </Card>
  )
}
