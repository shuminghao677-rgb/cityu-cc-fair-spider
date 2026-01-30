"use client"

import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { ArrowRight, TrendingUp } from "lucide-react"
import { Button } from "@/components/ui/button"
import { Progress } from "@/components/ui/progress"

const products = [
  {
    name: "/api/users",
    requests: "45.2K",
    percentage: 85,
    trend: "+12%",
  },
  {
    name: "/api/products",
    requests: "32.1K",
    percentage: 65,
    trend: "+8%",
  },
  {
    name: "/api/orders",
    requests: "28.4K",
    percentage: 55,
    trend: "+5%",
  },
  {
    name: "/api/analytics",
    requests: "21.8K",
    percentage: 42,
    trend: "+15%",
  },
  {
    name: "/api/auth",
    requests: "18.9K",
    percentage: 35,
    trend: "+3%",
  },
]

export function TopProducts() {
  return (
    <Card className="bg-card">
      <CardHeader className="flex flex-row items-center justify-between pb-2">
        <CardTitle className="text-base font-medium">Top Endpoints</CardTitle>
        <Button variant="ghost" size="icon" className="h-8 w-8">
          <ArrowRight className="h-4 w-4" />
        </Button>
      </CardHeader>
      <CardContent className="space-y-4">
        {products.map((product) => (
          <div key={product.name} className="space-y-2">
            <div className="flex items-center justify-between">
              <span className="text-sm font-medium text-foreground">{product.name}</span>
              <div className="flex items-center gap-2">
                <span className="text-sm text-muted-foreground">{product.requests}</span>
                <span className="flex items-center text-xs text-emerald-500">
                  <TrendingUp className="mr-0.5 h-3 w-3" />
                  {product.trend}
                </span>
              </div>
            </div>
            <Progress value={product.percentage} className="h-1.5" />
          </div>
        ))}
      </CardContent>
    </Card>
  )
}
