"""
STEM Fair 2026 - 专业与学历需求分析
输出：Excel 统计表 + JSON 仪表盘数据
"""
import pandas as pd
import os
import json

# 创建输出目录
os.makedirs("output/excel", exist_ok=True)
os.makedirs("output/dashboard", exist_ok=True)

df = pd.read_csv("stem_fair_2026_raw.csv", encoding="utf-8-sig")

# ========== 1. 专业 × 学历 原始统计 ==========
nested_analysis = {}
for _, row in df.iterrows():
    dep_names = [d.strip() for d in str(row["Department"]).split(",") if d.strip()]
    edu_names = [e.strip() for e in str(row["Education Level"]).split(",") if e.strip()]
    for d in dep_names:
        if d not in nested_analysis:
            nested_analysis[d] = {}
        for e in edu_names:
            if e not in nested_analysis[d]:
                nested_analysis[d][e] = 0
            nested_analysis[d][e] += 1

final_data = []
for dept, edu_dict in nested_analysis.items():
    for edu_level, count in edu_dict.items():
        final_data.append({"Department": dept, "Educational_Level": edu_level, "Count": count})

df_dep_edu = pd.DataFrame(final_data)

# ========== 2. 专业 × 学历 透视表 ==========
df_pivot = df_dep_edu.pivot_table(
    index="Department", columns="Educational_Level", values="Count", aggfunc="sum", fill_value=0
)
df_pivot.to_excel("output/excel/专业学历透视表.xlsx")

# ========== 3. 专业学历占比表 ==========
dept_totals = df_dep_edu.groupby("Department")["Count"].sum().reset_index(name="Total")
df_with_total = df_dep_edu.merge(dept_totals, on="Department")
df_with_total["Percentage"] = (df_with_total["Count"] / df_with_total["Total"] * 100).round(1)
df_with_total = df_with_total.sort_values(["Department", "Count"], ascending=[True, False])
df_with_total.to_excel("output/excel/专业学历占比表.xlsx", index=False)

# ========== 4. 各专业主学历表（每个专业最常见学历及占比） ==========
df_main_edu = (
    df_with_total.loc[df_with_total.groupby("Department")["Count"].idxmax()]
    [["Department", "Educational_Level", "Count", "Total", "Percentage"]]
    .reset_index(drop=True)
)
df_main_edu = df_main_edu.rename(columns={"Educational_Level": "Main_Education", "Percentage": "Main_Pct"})
df_main_edu.to_excel("output/excel/各专业主学历表.xlsx", index=False)

# ========== 5. 导出 JSON 供 v0 仪表盘使用 ==========
dashboard_data = {
    "education": {
        "pivot": {
            "departments": df_pivot.index.tolist(),
            "edu_levels": df_pivot.columns.tolist(),
            "matrix": df_pivot.values.tolist(),
        },
        "percentage": df_with_total.astype({"Count": int, "Total": int}).to_dict(orient="records"),
        "main_education": df_main_edu.astype({"Count": int, "Total": int}).to_dict(orient="records"),
        "edu_level_distribution": [
            {"education_level": k, "count": int(v)}
            for k, v in df_dep_edu.groupby("Educational_Level")["Count"].sum().sort_values(ascending=False).items()
        ],
        "department_distribution": [
            {"department": k, "count": int(v)}
            for k, v in df_dep_edu.groupby("Department")["Count"].sum().sort_values(ascending=False).items()
        ],
    }
}

with open("output/dashboard/education_analysis.json", "w", encoding="utf-8") as f:
    json.dump(dashboard_data, f, ensure_ascii=False, indent=2)

print("✓ 学历分析完成")
print(f"  - Excel: output/excel/专业学历透视表.xlsx, 专业学历占比表.xlsx, 各专业主学历表.xlsx")
print(f"  - JSON:  output/dashboard/education_analysis.json")
