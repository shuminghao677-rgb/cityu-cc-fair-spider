import sqlite3
import pandas as pd

# 读取 CSV 数据
df = pd.read_csv("stem_fair_2026_raw.csv", encoding="utf-8-sig")

# 标准化列名（空格转为下划线，便于 SQL 查询）
df.columns = [col.strip().replace(' ', '_') for col in df.columns]

# 连接 SQLite 数据库
conn = sqlite3.connect('stem_fair_2026.db')

# 将 DataFrame 写入数据库，自动创建表
# 表名: stem_fair_jobs
df.to_sql('stem_fair_jobs', conn, if_exists='replace', index=True, index_label='id')

# 创建索引以便查询
cursor = conn.cursor()
cursor.execute("CREATE INDEX IF NOT EXISTS idx_company ON stem_fair_jobs(Company_Name)")
cursor.execute("CREATE INDEX IF NOT EXISTS idx_department ON stem_fair_jobs(Department)")

conn.commit()
print(f"✓ 数据库创建成功！共导入 {len(df)} 条招聘记录")
print(f"  表名: stem_fair_jobs")
print(f"  列: {list(df.columns)}")

# 关闭连接
conn.close()
