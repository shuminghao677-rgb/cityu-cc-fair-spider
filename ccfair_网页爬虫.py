import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import time
from urllib.parse import urljoin

base_url="https://www.cityu.edu.hk/csci/news-events/events/2026/stem-career-fair-2026?JobDepartment=%7BBEDAA9D8-7D6A-45F1-8BD4-3D378700E446%7D&JobType=%7B2D4FFA7E-EC2D-4F80-856D-35E770A06676%7D&JobEduLevel=%7BE6C6AD4D-D7AE-40ED-8DCD-4FCF214BDB27%7D&q="
final_data=[]

response=requests.get(base_url)
soup=BeautifulSoup(response.text,"html.parser")
print("开始抓取")

interns=soup.find_all("tr",class_="col-md-12 mb-3")
for intern in interns:
    company_name=intern.find("td",class_="views-field views-field-field-company-name").p.get_text()
    job_title=intern.find("td",class_="views-field views-field-title").a.get_text()
    relative_path=intern.find("td",class_="views-field views-field-title").a["href"]
    detail_url=urljoin(base_url,relative_path)
    print(detail_url)

    detail_response=requests.get(detail_url)
    detail_soup=BeautifulSoup(detail_response.text,"html.parser")
    addr_tag=detail_soup.find("div",class_="clearfix text-formatted field field--name-field-application-procedure field--type-text-long field--label-above")

    if addr_tag:
        all_text=addr_tag.get_text(separator=" ",strip=True)
        urls=re.findall(r"https?://[^\s]+",all_text)#urls_lists
        emails=re.findall(r"[\w.-]+@[\w.-]+",all_text)#emails_lists

        total_addr=urls+emails

        addr_str=",".join(total_addr)
        if addr_str:
            print("此时申请地址是:   {addr_str}")
            application_addr=addr_str
        else:
            application_addr="暂未提供详细申请地址"

    else:
        application_addr="没有申请模块"
  
    
    final_data.append({"Company Name":company_name,"job Title":job_title,"Application Addr":application_addr})
    print(application_addr)
    time.sleep(1)
df=pd.DataFrame(final_data)
df.to_excel("cc_fair_cs专业实习招聘信息.xlsx",index=False)