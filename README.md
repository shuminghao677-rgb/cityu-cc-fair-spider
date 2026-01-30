# STEM Career Fair 2026 - 招聘数据分析

CityU CCFair 2026 招聘信息爬虫、数据库与 BI 仪表盘数据生成项目。

## 项目结构

```
├── ccfair_网页爬虫.py      # 从官网爬取招聘数据 → stem_fair_2026_raw.csv
├── sql_practice.py         # 将 CSV 导入 SQLite 数据库
├── departure_analysis.py   # 学历需求分析（专业×学历）
├── techinical_analysis.py  # 技术栈需求分析（专业×技能、行业×技能）
├── run_analysis.py         # 一键运行所有分析
├── output/
│   ├── excel/              # Excel 统计表
│   └── dashboard/          # JSON 数据（供 v0 仪表盘使用）
└── stem_fair_2026_raw.csv  # 原始数据（需先运行爬虫）
```

## 使用流程

### 1. 获取数据
```bash
python ccfair_网页爬虫.py   # 生成 stem_fair_2026_raw.csv
```

### 2. 建立数据库
```bash
python sql_practice.py      # 生成 stem_fair_2026.db
```

### 3. 运行分析
```bash
python run_analysis.py      # 依次执行学历分析 + 技术栈分析
```

或分别运行：
```bash
python departure_analysis.py
python techinical_analysis.py
```

## 输出说明

### Excel（output/excel/）

| 学历分析 | 技术栈分析 |
|----------|------------|
| 专业学历透视表 | 专业技能透视表 |
| 专业学历占比表 | 各专业Top技能汇总表 |
| 各专业主学历表 | 行业技能统计表 |
| | 全行业技能排名表 |

### JSON 仪表盘数据（output/dashboard/）

供 v0 或前端 BI 仪表盘使用：

- `education_analysis.json` - 学历相关图表数据
- `technical_analysis.json` - 技术栈相关图表数据  
- `dashboard_data.json` - 合并后的完整数据（推荐入口）

#### JSON 数据结构示例

```json
{
  "education": {
    "pivot": { "departments": [], "edu_levels": [], "matrix": [] },
    "percentage": [],
    "main_education": [],
    "edu_level_distribution": [],
    "department_distribution": []
  },
  "technical": {
    "major_skill_pivot": { "majors": [], "skills": [], "matrix": [] },
    "top_skills_by_major": {},
    "skill_ranking": [],
    "industry_skill": [],
    "industry_distribution": []
  }
}
```

## v0 仪表盘集成

1. 将本项目推送到 GitHub
2. 在 v0 中创建新项目，引入 `output/dashboard/dashboard_data.json`
3. 使用数据结构中的 `education`、`technical` 渲染：
   - 热力图：`pivot.matrix` + `departments`/`edu_levels` 或 `majors`/`skills`
   - 柱状图：`skill_ranking`、`edu_level_distribution`、`department_distribution`
   - 饼图：`industry_distribution`、`main_education`
   - 表格：`percentage`、`top_skills_by_major`

## 依赖

```
pandas
requests
beautifulsoup4
openpyxl  # Excel 输出
```

## License

MIT
