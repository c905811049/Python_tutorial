import requests
import json
import time
import xlwt

# 初始化Excel和表格
wb = xlwt.Workbook()
ws = wb.add_sheet('BOSS_Jobs')

# 设置表头
headers = ['职务名称', '公司', '城市', '薪水', '经验', '教育水平', '行业', '技能', 'dt', 'boss']
for i, header in enumerate(headers):
    ws.write(0, i, header)

# 初始化行数
row_num = 1

keys = ["etl"]

for key in keys:
    cookie = '__g=-; __l=l=%2Fwww.zhipin.com%2Fweb%2Fgeek%2Fjob%3Fquery%3Detc%26city%3D101300100&r=&g=&s=3&friend_source=0; wd_guid=81c29a55-d1df-4db7-9387-86439a60c509; historyState=state; _bl_uid=F8lywlX6uRqsU6sqwitzqRsvasL7; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1693222224; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1693222224; __zp_stoken__=395deZ01rBSlgP2phABE%2FIHxlWBAseQ1KLCwke3VuJhtDP3wULkArNmEsVRI0HXgGPGRKf3NIBkIGOzs3dQBzYQ9MGxFMK2UJOmEReFR2CQkcAw5QMgkXJV4UGCR6FkFNfl14ACBOC0c2IT4%3D; __c=1693222220; __a=67065309.1693222220..1693222220.2.1.2.2'
    ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
    head = {'Cookie': cookie, 'User-Agent': ua}
    
    url = f"https://www.zhipin.com/wapi/zpgeek/search/joblist.json?scene=1&query={key}&city=100010000&experience=&payType=&partTime=&degree=&industry=&scale=&stage=&position=&jobType=&salary=&multiBusinessDistrict=&multiSubway=&page=1&pageSize=30"
    
    time.sleep(5)
    res = requests.get(url, headers=head)
    data = json.loads(res.text)
    
    for job in data['zpData']['jobList']:
        jobname = job['jobName']
        company = job['brandName']
        city = job['city']
        sal = job['salaryDesc']
        exp = job['jobExperience']
        edu = job['jobDegree']
        industry = job['brandIndustry']
        skill = ','.join(job['skills'])  # 将技能列表转换为逗号分隔的字符串
        dt = job['lastModifyTime']
        boss = job['bossName']
        
        # 写入数据到Excel
        row_data = [jobname, company, city, sal, exp, edu, industry, skill, dt, boss]
        for i, item in enumerate(row_data):
            ws.write(row_num, i, item)
        
        row_num += 1

# 保存Excel文件
wb.save('BOSS_Job_Data.xls')
