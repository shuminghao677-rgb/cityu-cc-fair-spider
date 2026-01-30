"use client"

import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import {
  PieChart,
  Pie,
  Cell,
  ResponsiveContainer,
  Legend,
  Tooltip,
} from "recharts"

const educationData = [
  { name: "Bachelor's", value: 2088, percentage: 46.4 },
  { name: "Master's", value: 1393, percentage: 31.0 },
  { name: "Doctoral", value: 1019, percentage: 22.6 },
]

const COLORS = ["#3b82f6", "#10b981", "#f59e0b"]

const renderCustomLabel = ({
  cx,
  cy,
  midAngle,
  innerRadius,
  outerRadius,
  percent,
}: {
  cx: number
  cy: number
  midAngle: number
  innerRadius: number
  outerRadius: number
  percent: number
}) => {
  const RADIAN = Math.PI / 180
  const radius = innerRadius + (outerRadius - innerRadius) * 0.5
  const x = cx + radius * Math.cos(-midAngle * RADIAN)
  const y = cy + radius * Math.sin(-midAngle * RADIAN)

  return (
    <text
      x={x}
      y={y}
      fill="white"
      textAnchor="middle"
      dominantBaseline="central"
      fontSize={12}
      fontWeight={600}
    >
      {`${(percent * 100).toFixed(0)}%`}
    </text>
  )
}

export function EducationChart() {
  return (
    <Card className="bg-card">
      <CardHeader>
        <CardTitle className="text-base font-medium">
          Education Level Distribution
        </CardTitle>
        <p className="text-sm text-muted-foreground">
          Required education levels across all positions
        </p>
      </CardHeader>
      <CardContent>
        <div className="h-[300px]">
          <ResponsiveContainer width="100%" height="100%">
            <PieChart>
              <Pie
                data={educationData}
                cx="50%"
                cy="50%"
                labelLine={false}
                label={renderCustomLabel}
                outerRadius={100}
                innerRadius={50}
                dataKey="value"
                stroke="none"
              >
                {educationData.map((_, index) => (
                  <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
                ))}
              </Pie>
              <Tooltip
                contentStyle={{
                  backgroundColor: "#18181b",
                  border: "1px solid #27272a",
                  borderRadius: "8px",
                  color: "#fafafa",
                }}
                formatter={(value: number) => [`${value} positions`, "Count"]}
              />
              <Legend
                verticalAlign="bottom"
                height={36}
                formatter={(value) => (
                  <span style={{ color: "#a1a1aa", fontSize: "12px" }}>{value}</span>
                )}
              />
            </PieChart>
          </ResponsiveContainer>
        </div>
        <div className="mt-4 grid grid-cols-3 gap-4">
          {educationData.map((item, index) => (
            <div key={item.name} className="text-center">
              <div
                className="mx-auto mb-1 h-2 w-2 rounded-full"
                style={{ backgroundColor: COLORS[index] }}
              />
              <p className="text-lg font-semibold text-foreground">{item.value}</p>
              <p className="text-xs text-muted-foreground">{item.name}</p>
            </div>
          ))}
        </div>
      </CardContent>
    </Card>
  )
}
