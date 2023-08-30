from time import sleep
import pymysql
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 任务需求:爬取数据信息导入数据库
'''
https://www.51job.com/

爬取大数据岗位  ETL  BI岗位
爬取信息写入excel，爬个10页
岗位名字
公司名字
薪水
地区 
年限
学历
公司的行业
技能福利
日期
解决翻页    元素.click()
for 
'''
'''
CREATE TABLE `job_51_boss` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `jobname` varchar(60) DEFAULT NULL,
  `company` varchar(250) DEFAULT NULL,
  `city` varchar(250) DEFAULT NULL,
  `sal` varchar(250) DEFAULT NULL,
  `exp` varchar(250) DEFAULT NULL,
  `edu` varchar(250) DEFAULT NULL,
  `industry` varchar(250) DEFAULT NULL,
  `skill` varchar(250) DEFAULT NULL,
  `dt` varchar(250) DEFAULT NULL,
  `source` varchar(250) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=945 DEFAULT CHARSET=utf8;
'''
con = pymysql.Connect(host="localhost",port=3306,user="root",passwd="admin",db="db",charset="utf8")


# 创建一个新的 Edge 会话
driver = webdriver.Edge()


url = 'https://www.51job.com/'

driver.get(url)

driver.implicitly_wait(10)

jobtitle=['ETL','BI']

for item in jobtitle:
    driver.find_element(By.ID,"kwdselectid").send_keys(item)
    driver.find_element(By.CSS_SELECTOR,'body > div.content > div > div.fltr.radius_5 > div > button').click()

    for i in range(1,51):
        elelist=driver.find_elements(By.CLASS_NAME,'e.sensors_exposure')
        for ele in elelist:
            # 岗位名称
            jobname = ele.find_element(By.CLASS_NAME,'jname.at').text
            # 公司名字
            company = ele.find_element(By.CLASS_NAME,'cname.at').text
            # 地区
            city=ele.find_element(By.CSS_SELECTOR,'#app > div > div.post > div > div > div.j_result > div > div:nth-child(2) > div > div:nth-child(2) > div.j_joblist > div:nth-child(2) > div.el > p.info > span.d.at > span:nth-child(1)').text
            # 薪水
            sal=ele.find_element(By.CLASS_NAME,'sal').text
            # 年限
            exp=ele.find_element(By.CSS_SELECTOR,'#app > div > div.post > div > div > div.j_result > div > div:nth-child(2) > div > div:nth-child(2) > div.j_joblist > div:nth-child(2) > div.el > p.info > span.d.at > span:nth-child(3)').text
            # 公司的行业
            industry=ele.find_element(By.CLASS_NAME,'int.at').text
            # 存储技能福利标签
            sk=[]
            # 遍历技能福利标签的元素
            skill=ele.find_elements(By.CLASS_NAME,'tags')
            for item in skill:
                tag = item.find_element(By.TAG_NAME,'span').text
            # 学历
            dt=ele.find_element(By.CSS_SELECTOR,'#app > div > div.post > div > div > div.j_result > div > div:nth-child(2) > div > div:nth-child(2) > div.j_joblist > div:nth-child(4) > div.el > p.info > span.d.at > span:nth-child(5)').text
            #
            source=ele.find_element(By.CLASS_NAME,'dc。at').text
        # 点击下一页
        driver.find_element(By.CSS_SELECTOR, '#app > div > div.post > div > div > div.j_result > div > div:nth-child(2) > div > div.bottom-page > div > div > div > button.btn-next').click()
        sleep(5)
    sleep(5)

driver.quit()