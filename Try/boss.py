import requests
import time
import json
import pandas as pd

# 初始化空的DataFrame用于存储数据
df = pd.DataFrame(columns=['jobname', 'company', 'city', 'sal', 'exp', 'edu', 'industry', 'skill', 'dt', 'boss'])

keys = ["etl", "大数据开发", "运维开发", "bi"]

for key in keys:
    cookie = 'lastCity=101300100; wd_guid=eaf35c5f-fc6b-4035-a4de-13c51fe03305; historyState=state; _bl_uid=XjlbLi2tk2U2RL1zn727jhLunR1t; YD00951578218230%3AWM_TID=dv5Tdw02T5xBQUVQQUPVg7KItQeS%2BBqj; gdxidpyhxdE=ayvC89ELtAmBANTd%2FEd38uu3IXIoOdEBBibomk%5CKozLaTrgPOsoY1TksaWcHBn4DS1CvjNlqPDQHW8a1GUTcgZRJSZkI1dWigOGHtyGbrCZzjoIfEbkecXpB2mZCQaVoZPmQuaMqhijZrMmHiDfJJuVtjw7Io%2BRkpCVTyc5fepa4iEzH%3A1692192016402; YD00951578218230%3AWM_NI=e3qEyyQuNt%2BKYGQb%2F8B6HxQ4SUBjblHVaqEGy9n%2FwfNKbkqM5rTy%2B99UOribUaUNbe4XgJBy6CVFT3qHhI2etGWnZ%2BPDduAf7VY9WLk%2B%2BzHBWAQm4vMiLfUUOInjFHEHRk8%3D; YD00951578218230%3AWM_NIKE=9ca17ae2e6ffcda170e2e6ee8ff05390e7a69bd34b95ac8bb3d85b978a8fb0d16db6e9fbb0e665ab9a8f96cc2af0fea7c3b92aa7edbfa6fc7393ab8295aa419b999f83ae3482ea8899d440918b8e8be1688c8aaf92c84dbbe7a2d0f66e8e95ae8cf447f7ae9c9aaa33fb8b8193ec6a97bf9bafe16ff888a9abc173f69d9aa7d739b398a8aab16fb899998fd921949cac96c46ef58a97dad648a9f5e59bcb4a959f9f8eb77e8fb78487d85f8d97a28bc54487989e8cbb37e2a3; __zp_seo_uuid__=29e6d895-952a-4e34-a886-276f62592f8d; __g=-; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1692861395,1692944045,1693195895,1693214972; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1693214972; __zp_stoken__=395deZ01rBSlgP0AIFWkqIHxlWBB7bmJSIHske3VuJiJASS4aPEArNmEsYXAQMW0GPGRKf3NIIDoGEU03aQdmVygQXE8TUXsXH3AgeFR2CQkcAw5FHi11EV4UGCR6BEFNfl14ACBOC0c2IT4%3D; __c=1693214972; __l=r=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3Dva8bueh3bzymHW1LhZyClLqPIfsqNcW1JtHDSopKOAPe7r-gJC3al2DUGnlbCiOx%26wd%3D%26eqid%3Dc318832c000f5b730000000664ec68f9&l=%2Fwww.zhipin.com%2Fweb%2Fgeek%2Fjob%3Fquery%3DETL%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588%26city%3D100010000&s=3&g=&friend_source=0&s=3&friend_source=0; __a=10765778.1686042249.1693195895.1693214972.113.14.4.7'  # 请替换为你的Cookie
    ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.62'  # 请替换为你的User-Agent
    head = {'Cookie': cookie, 'User-Agent': ua}
    
    url = f"https://www.zhipin.com/wapi/zpgeek/search/joblist.json?scene=1&query={key}&city=100010000&experience=&payType=&partTime=&degree=&industry=&scale=&stage=&position=&jobType=&salary=&multiBusinessDistrict=&multiSubway=&page=1&pageSize=30"
    
    time.sleep(5)  # 暂停5秒，以防止请求过于频繁
    res = requests.get(url, headers=head)
    data = json.loads(res.text)
    
    for job in data['data']['list']:
        jobname = job['jobName']
        company = job['companyName']
        city = job['city']
        sal = job['salary']
        exp = job['workYear']
        edu = job['education']
        industry = job['industryName']
        skill = job['skillLables']
        dt = job['updateTime']
        boss = job['bossName']
        
        # 将数据添加到DataFrame
        df = df.append({'jobname': jobname, 'company': company, 'city': city, 'sal': sal, 'exp': exp, 'edu': edu, 'industry': industry, 'skill': skill, 'dt': dt, 'boss': boss}, ignore_index=True)

# 将DataFrame保存为Excel文件
df.to_excel("BOSS_Job_Data.xlsx", index=False)
