import pandas as pd
import re
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


df=pd.read_csv("stem_fair_2026_raw.csv")

tech_keywords = {
    "AEC & Built Environment": ["autocad", "revit", "bim", "civil 3d", "sketchup", "surveying", "qs", "structural"],
    "Energy & Sustainability": ["renewable", "solar", "wind energy", "sustainability", "hvac", "power system", "carbon"],
    "Bio & Healthcare": ["r language", "sas", "bioinformatics", "molecular", "clinical", "biostatistics", "medical device"],
    "Electronics & Info": ["pcb", "fpga", "plc", "embedded", "circuit", "verilog", "microcontroller", "semiconductor"],
    "Mechanical & Aero": ["solidworks", "catia", "ansys", "fea", "robotics", "cnc", "thermodynamics", "manufacturing"],
    "CS & FinTech": ["python", "java", "c\+\+", "machine learning", "blockchain", "cybersecurity", "sql", "aws", "fintech"]
}
final_results=[]
for index,row in df.iterrows():#先得到每个职位的信息
    job_content=str(row.get("Job description","")).lower()#获得每一行职位的工作要求 获得里面 key是”Job Description“的那一行用get 前面是key 后面是 default
    deps=[d.strip() for d in str(row["Department"]).split(",")]#这里是用str前面用，逗号split 获得list 【d.strip() for d in list】

    found_skills=set()#这里新建一个list 和 set是等效的但是用set更严谨 这里看skill到底有没有出现在job content中
    for category,skills in tech_keywords.items():#只有遍历字典的时候 需要items（）
        for sk in skills:#这里skills是list 所以遍历他的时候 直接for就行了
            if sk in job_content:
                found_skills.add((category,sk))#有的话就生成元祖 这里因为是在add里面添加元祖需要两个括号
    for category,sk in found_skills:#这里是遍历list中的每个元祖然后出现在这个职位的所有skill 都会新加上这个职位对应招聘的专业 生成字典
        for d in deps:
            final_results.append({"Industry":category,"Major":d,"Skill":sk,})

df_technique=pd.DataFrame(final_results)
df_analysis_each_skill=df_technique.groupby(["Major","Skill"]).size().reset_index(name="Frequency")
df_analysis_each_skill=df_analysis_each_skill.sort_values(by=["Major","Frequency"],ascending=[True,False])

df_analysis_total_skill=df_technique.groupby(["Skill"]).size().reset_index(name="Total Frequency")
df_analysis_total_skill=df_analysis_total_skill.sort_values(by=["Total Frequency"],ascending=False)

df_analysis_each_skill.to_excel("技术栈需求各行业高频统计.xlsx",index=False)
df_analysis_total_skill.to_excel("技术栈需求全行业高频统计.xlsx",index=False)
