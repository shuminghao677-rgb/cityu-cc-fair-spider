import pandas as pd
from collections import Counter
import re
dep_name_list=[]
df=pd.read_csv("stem_fair_2026_raw.csv")
nested_analysis = {}
for index,row in df.iterrows():
    dep_names=[d.strip() for d in str(row["Department"]).split(",")]
    edu_names=[e.strip() for e in str(row["Education Level"]).split(",")]
    for d in dep_names:
        if d not in nested_analysis:
            nested_analysis[d]={}
        for e in edu_names:
            if e not in nested_analysis[d]:
                nested_analysis[d][e]=0
            nested_analysis[d][e]+=1
final_data=[]
for key1,key2 in nested_analysis.items():
    for key2,value in nested_analysis[key1].items():
        final_data.append({"Department":key1,"Educational Level":key2,"Count":value})
df_dep_edu=pd.DataFrame(final_data)
df_dep_edu.to_excel("高频学科统计.xlsx",index=False)
