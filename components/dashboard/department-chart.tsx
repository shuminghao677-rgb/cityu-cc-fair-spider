"use client"

import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
  Cell,
} from "recharts"

const data = [
  { name: "EE Engineering", total: 254 },
  { name: "Mechanical Eng", total: 252 },
  { name: "Computer Science", total: 185 },
  { name: "Info Engineering", total: 172 },
  { name: "Civil Engineering", total: 163 },
  { name: "Computer & Data", total: 156 },
  { name: "Env Science", total: 154 },
  { name: "Electronic Comm", total: 153 },
  { name: "Materials Sci", total: 147 },
  { name: "Data Systems", total: 146 },
]

const COLORS = [
  "#3b82f6",
  "#3b82f6",
  "#3b82f6",
  "#60a5fa",
  "#60a5fa",
  "#60a5fa",
  "#93c5fd",
  "#93c5fd",
  "#93c5fd",
  "#93c5fd",
]

export function DepartmentChart() {
  return (
    <Card className="bg-card">
      <CardHeader>
        <CardTitle className="text-base font-medium">
          Top Departments by Job Positions
        </CardTitle>
        <p className="text-sm text-muted-foreground">
          Number of positions available per department
        </p>
      </CardHeader>
      <CardContent>
        <div className="h-[300px]">
          <ResponsiveContainer width="100%" height="100%">
            <BarChart
              data={data}
              layout="vertical"
              margin={{ top: 0, right: 20, left: 0, bottom: 0 }}
            >
              <CartesianGrid strokeDasharray="3 3" stroke="#27272a" horizontal={false} />
              <XAxis type="number" stroke="#71717a" fontSize={12} tickLine={false} />
              <YAxis
                type="category"
                dataKey="name"
                stroke="#71717a"
                fontSize={11}
                tickLine={false}
                axisLine={false}
                width={100}
              />
              <Tooltip
                contentStyle={{
                  backgroundColor: "#18181b",
                  border: "1px solid #27272a",
                  borderRadius: "8px",
                  color: "#fafafa",
                }}
                labelStyle={{ color: "#fafafa" }}
                cursor={{ fill: "#27272a" }}
              />
              <Bar dataKey="total" radius={[0, 4, 4, 0]}>
                {data.map((_, index) => (
                  <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
                ))}
              </Bar>
            </BarChart>
          </ResponsiveContainer>
        </div>
      </CardContent>
    </Card>
  )
}
