"""
STEM Fair 2026 - 技术栈需求分析
输出：Excel 统计表 + JSON 仪表盘数据
"""
import pandas as pd
import os
import json

os.makedirs("output/excel", exist_ok=True)
os.makedirs("output/dashboard", exist_ok=True)

df = pd.read_csv("stem_fair_2026_raw.csv", encoding="utf-8-sig")

tech_keywords = {
    "AEC & Built Environment": ["autocad", "revit", "bim", "civil 3d", "sketchup", "surveying", "qs", "structural"],
    "Energy & Sustainability": ["renewable", "solar", "wind energy", "sustainability", "hvac", "power system", "carbon"],
    "Bio & Healthcare": ["r language", "sas", "bioinformatics", "molecular", "clinical", "biostatistics", "medical device"],
    "Electronics & Info": ["pcb", "fpga", "plc", "embedded", "circuit", "verilog", "microcontroller", "semiconductor"],
    "Mechanical & Aero": ["solidworks", "catia", "ansys", "fea", "robotics", "cnc", "thermodynamics", "manufacturing"],
    "CS & FinTech": ["python", "java", "c++", "machine learning", "blockchain", "cybersecurity", "sql", "aws", "fintech"],
}

final_results = []
for _, row in df.iterrows():
    job_content = str(row.get("Job description", "")).lower()
    deps = [d.strip() for d in str(row["Department"]).split(",") if d.strip()]
    found_skills = set()
    for category, skills in tech_keywords.items():
        for sk in skills:
            if sk in job_content:
                found_skills.add((category, sk))
    for category, sk in found_skills:
        for d in deps:
            final_results.append({"Industry": category, "Major": d, "Skill": sk})

df_technique = pd.DataFrame(final_results)

# ========== 1. 专业 × 技能 透视表 ==========
df_major_skill = df_technique.groupby(["Major", "Skill"]).size().reset_index(name="Frequency")
df_pivot = df_major_skill.pivot_table(
    index="Major", columns="Skill", values="Frequency", aggfunc="sum", fill_value=0
)
df_pivot.to_excel("output/excel/专业技能透视表.xlsx")

# ========== 2. 各专业 Top 技能汇总表（每专业 Top 10） ==========
df_ranked = df_major_skill.sort_values(["Major", "Frequency"], ascending=[True, False])
top_n = 10
df_top_skills = df_ranked.groupby("Major").head(top_n).reset_index(drop=True)
df_top_skills["Rank"] = df_top_skills.groupby("Major").cumcount() + 1
df_top_skills.to_excel("output/excel/各专业Top技能汇总表.xlsx", index=False)

# ========== 3. 行业 × 技能 统计表 ==========
df_industry_skill = df_technique.groupby(["Industry", "Skill"]).size().reset_index(name="Frequency")
df_industry_skill = df_industry_skill.sort_values(["Industry", "Frequency"], ascending=[True, False])
df_industry_skill.to_excel("output/excel/行业技能统计表.xlsx", index=False)

# ========== 4. 全行业技能排名表（已有） ==========
df_total_skill = df_technique.groupby("Skill").size().reset_index(name="Total_Frequency")
df_total_skill = df_total_skill.sort_values("Total_Frequency", ascending=False)
df_total_skill.to_excel("output/excel/全行业技能排名表.xlsx", index=False)

# ========== 5. 导出 JSON 供 v0 仪表盘使用 ==========
# 专业×技能 矩阵
pivot_json = {
    "majors": df_pivot.index.tolist(),
    "skills": df_pivot.columns.tolist(),
    "matrix": df_pivot.values.tolist(),
}

# 各专业 Top 技能
top_skills_by_major = {}
for major in df_top_skills["Major"].unique():
    subset = df_top_skills[df_top_skills["Major"] == major]
    top_skills_by_major[major] = [
        {"skill": r["Skill"], "frequency": int(r["Frequency"]), "rank": int(r["Rank"])}
        for _, r in subset.iterrows()
    ]

# 全行业技能排名
skill_ranking = [{"skill": r["Skill"], "frequency": int(r["Total_Frequency"])} for _, r in df_total_skill.iterrows()]

# 行业技能分布
industry_skill_list = [
    {"industry": r["Industry"], "skill": r["Skill"], "frequency": int(r["Frequency"])}
    for _, r in df_industry_skill.iterrows()
]

# 行业分布
industry_distribution = [
    {"industry": k, "count": int(v)}
    for k, v in df_technique.groupby("Industry").size().sort_values(ascending=False).items()
]

dashboard_data = {
    "technical": {
        "major_skill_pivot": pivot_json,
        "top_skills_by_major": top_skills_by_major,
        "skill_ranking": skill_ranking,
        "industry_skill": industry_skill_list,
        "industry_distribution": industry_distribution,
    }
}

with open("output/dashboard/technical_analysis.json", "w", encoding="utf-8") as f:
    json.dump(dashboard_data, f, ensure_ascii=False, indent=2)

print("✓ 技术栈分析完成")
print(f"  - Excel: output/excel/专业技能透视表.xlsx, 各专业Top技能汇总表.xlsx, 行业技能统计表.xlsx, 全行业技能排名表.xlsx")
print(f"  - JSON:  output/dashboard/technical_analysis.json")
