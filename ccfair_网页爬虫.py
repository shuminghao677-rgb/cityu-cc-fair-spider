import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import time
from urllib.parse import urljoin
from pyecharts.charts import Bar
from pyecharts import options as opts

final_data=[]

for i in range(0,4):
    base_url1="https://www.cityu.edu.hk/csci/news-events/events/2026/stem-career-fair-2026?page="
    base_url=base_url1+str(i)
    print(base_url)

    response=requests.get(base_url)
    soup=BeautifulSoup(response.text,"html.parser")
    print(f"开始抓取第{i+1}页")

    interns=soup.find_all("tr",class_="col-md-12 mb-3")
    for intern in interns:
        try:
            company_name=intern.find("td",class_="views-field views-field-field-company-name").p.get_text()
            job_title=intern.find("td",class_="views-field views-field-title").a.get_text()
            department_text=intern.find("td",class_="views-field views-field-field-department").get_text()
            education_text=intern.find("td",class_="views-field views-field-field-education-level").get_text()
            relative_path=intern.find("td",class_="views-field views-field-title").a["href"]
            detail_url=urljoin(base_url,relative_path)
            print(detail_url)
    
            detail_response=requests.get(detail_url)
            detail_soup=BeautifulSoup(detail_response.text,"html.parser")
            #抓取job description
            job_description=detail_soup.find("div",class_="clearfix text-formatted field field--name-body field--type-text-with-summary field--label-above")
            job_text=job_description.get_text(strip=True)if job_description else ""
            job_text_clear=job_text.replace("Job Description","").strip()

            application_procedure=detail_soup.find("div",class_="clearfix text-formatted field field--name-field-application-procedure field--type-text-long field--label-above")
            app_text=application_procedure.get_text(strip=True) if application_procedure else ""
            app_text_clear=app_text.replace("Application Procedure","").strip()

            


            final_data.append({"Company Name":company_name,"Job Title":job_title,"Job description":job_text_clear,"Application Procedure":app_text_clear,"Education Level": education_text,"Department":department_text})
            print(f"目前抓取到公司是{company_name}")
            time.sleep(0.5)
        except Exception as e:
            print(f"抓取{detail_url}时失败,失败原因是{e}")
            continue


df=pd.DataFrame(final_data)
df.to_csv("stem_fair_2026_raw.csv",index=False,encoding="utf-8-sig")
