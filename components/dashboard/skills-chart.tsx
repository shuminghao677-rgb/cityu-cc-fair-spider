"use client"

import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
} from "recharts"

const skillsData = [
  { name: "Python", count: 892 },
  { name: "SQL", count: 756 },
  { name: "Machine Learning", count: 634 },
  { name: "Data Analysis", count: 589 },
  { name: "JavaScript", count: 478 },
  { name: "Java", count: 423 },
  { name: "Cloud Computing", count: 387 },
  { name: "Deep Learning", count: 345 },
]

export function SkillsChart() {
  return (
    <Card className="bg-card">
      <CardHeader className="pb-2">
        <CardTitle className="text-base font-medium">
          Top Technical Skills
        </CardTitle>
        <p className="text-sm text-muted-foreground">
          Most demanded skills across positions
        </p>
      </CardHeader>
      <CardContent>
        <div className="h-[250px]">
          <ResponsiveContainer width="100%" height="100%">
            <BarChart
              data={skillsData}
              layout="vertical"
              margin={{ top: 0, right: 20, left: 0, bottom: 0 }}
            >
              <XAxis type="number" stroke="#71717a" fontSize={11} tickLine={false} axisLine={false} />
              <YAxis
                type="category"
                dataKey="name"
                stroke="#71717a"
                fontSize={11}
                tickLine={false}
                axisLine={false}
                width={90}
              />
              <Tooltip
                contentStyle={{
                  backgroundColor: "#18181b",
                  border: "1px solid #27272a",
                  borderRadius: "8px",
                  color: "#fafafa",
                }}
                cursor={{ fill: "#27272a" }}
              />
              <Bar dataKey="count" fill="#10b981" radius={[0, 4, 4, 0]} />
            </BarChart>
          </ResponsiveContainer>
        </div>
      </CardContent>
    </Card>
  )
}
