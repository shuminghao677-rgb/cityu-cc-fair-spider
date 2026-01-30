"use client"

import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"

const skillCategories = [
  {
    category: "Programming",
    skills: [
      { name: "Python", level: 95 },
      { name: "Java", level: 72 },
      { name: "JavaScript", level: 68 },
      { name: "C++", level: 54 },
    ],
  },
  {
    category: "Data & AI",
    skills: [
      { name: "ML/AI", level: 88 },
      { name: "Data Analysis", level: 82 },
      { name: "Deep Learning", level: 65 },
      { name: "NLP", level: 48 },
    ],
  },
  {
    category: "Infrastructure",
    skills: [
      { name: "Cloud", level: 76 },
      { name: "SQL", level: 85 },
      { name: "Docker", level: 58 },
      { name: "Linux", level: 62 },
    ],
  },
]

function getColorByLevel(level: number): string {
  if (level >= 80) return "bg-emerald-500"
  if (level >= 60) return "bg-blue-500"
  if (level >= 40) return "bg-amber-500"
  return "bg-zinc-600"
}

export function SkillsHeatmap() {
  return (
    <Card className="bg-card">
      <CardHeader className="pb-2">
        <CardTitle className="text-base font-medium">
          Skills Demand Heatmap
        </CardTitle>
        <p className="text-sm text-muted-foreground">
          Demand intensity by category
        </p>
      </CardHeader>
      <CardContent>
        <div className="space-y-4">
          {skillCategories.map((category) => (
            <div key={category.category}>
              <p className="mb-2 text-xs font-medium text-muted-foreground">
                {category.category}
              </p>
              <div className="grid grid-cols-4 gap-1">
                {category.skills.map((skill) => (
                  <div
                    key={skill.name}
                    className={`flex flex-col items-center justify-center rounded-md p-2 ${getColorByLevel(
                      skill.level
                    )}`}
                  >
                    <span className="text-[10px] font-medium text-white">
                      {skill.name}
                    </span>
                    <span className="text-[9px] text-white/80">{skill.level}%</span>
                  </div>
                ))}
              </div>
            </div>
          ))}
        </div>

        <div className="mt-4 flex items-center justify-center gap-4 text-[10px] text-muted-foreground">
          <div className="flex items-center gap-1">
            <div className="h-2 w-2 rounded-sm bg-emerald-500" />
            <span>High</span>
          </div>
          <div className="flex items-center gap-1">
            <div className="h-2 w-2 rounded-sm bg-blue-500" />
            <span>Medium</span>
          </div>
          <div className="flex items-center gap-1">
            <div className="h-2 w-2 rounded-sm bg-amber-500" />
            <span>Low</span>
          </div>
        </div>
      </CardContent>
    </Card>
  )
}
