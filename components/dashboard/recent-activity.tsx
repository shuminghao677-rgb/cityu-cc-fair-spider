"use client"

import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { ArrowRight, AlertCircle, CheckCircle2, Clock, XCircle } from "lucide-react"
import { Button } from "@/components/ui/button"
import { cn } from "@/lib/utils"

const activities = [
  {
    id: 1,
    type: "success",
    message: "Deployment completed successfully",
    time: "2 min ago",
    icon: CheckCircle2,
  },
  {
    id: 2,
    type: "warning",
    message: "High memory usage detected",
    time: "15 min ago",
    icon: AlertCircle,
  },
  {
    id: 3,
    type: "error",
    message: "Failed to connect to database",
    time: "32 min ago",
    icon: XCircle,
  },
  {
    id: 4,
    type: "info",
    message: "Scheduled maintenance in 2 hours",
    time: "1 hour ago",
    icon: Clock,
  },
  {
    id: 5,
    type: "success",
    message: "New user registration spike",
    time: "2 hours ago",
    icon: CheckCircle2,
  },
]

const typeStyles = {
  success: "text-emerald-500",
  warning: "text-amber-500",
  error: "text-red-500",
  info: "text-blue-500",
}

export function RecentActivity() {
  return (
    <Card className="bg-card">
      <CardHeader className="flex flex-row items-center justify-between pb-2">
        <CardTitle className="text-base font-medium">Recent Activity</CardTitle>
        <Button variant="ghost" size="icon" className="h-8 w-8">
          <ArrowRight className="h-4 w-4" />
        </Button>
      </CardHeader>
      <CardContent className="space-y-3">
        {activities.map((activity) => (
          <div
            key={activity.id}
            className="flex items-start gap-3 rounded-lg p-2 transition-colors hover:bg-secondary/50"
          >
            <activity.icon
              className={cn("mt-0.5 h-4 w-4", typeStyles[activity.type as keyof typeof typeStyles])}
            />
            <div className="flex-1 space-y-0.5">
              <p className="text-sm text-foreground">{activity.message}</p>
              <p className="text-xs text-muted-foreground">{activity.time}</p>
            </div>
          </div>
        ))}
      </CardContent>
    </Card>
  )
}
