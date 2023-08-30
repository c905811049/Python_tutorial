from time import sleep
import pymysql
from selenium import webdriver
from selenium.webdriver.common.by import By
# MySQL数据库连接
con = pymysql.Connect(host="localhost", port=3306, user="root", passwd="admin", db="db", charset="utf8")
cursor = con.cursor()

# 创建Edge会话
driver = webdriver.Edge()


url = 'https://www.51job.com/'


jobtitle = ['BI','大数据','运维','实施']

for item in jobtitle:
    sleep(5)
    print("正在爬取:",item)
    try:
        driver.get(url)
        driver.implicitly_wait(10)
        driver.find_element(By.ID, "kwdselectid").send_keys(item)
        driver.find_element(By.CSS_SELECTOR, 'body > div.content > div > div.fltr.radius_5 > div > button').click()
        sleep(5)
        print("已经点击")
        for i in range(1, 11):  # 爬取10页
            print("正在打印第:",i)
            elelist = driver.find_elements(By.CLASS_NAME, 'e.sensors_exposure')
            for ele in elelist:
                try:
                    # 岗位名称
                    jobname = ele.find_element(By.CLASS_NAME, 'jname.at').text
                    # 公司名字
                    company = ele.find_element(By.CLASS_NAME, 'cname.at').text
                    # 地区
                    # 找到包含所有信息的父span标签
                    parent_span = ele.find_element(By.CSS_SELECTOR, 'span.d.at')

                    # 在父span标签下找到所有的子span标签
                    child_spans = parent_span.find_elements(By.TAG_NAME, 'span')

                    # 获取第一个子span标签的文本内容
                    city_full = child_spans[0].text  # "上海·浦东新区"

                    # 薪水
                    sal = ele.find_element(By.CLASS_NAME, 'sal').text
                    # 年限
                    # 找到包含所有信息的父span标签
                    parent_span = ele.find_element(By.CSS_SELECTOR, 'span.d.at')
                    
                    # 在父span标签下找到所有的子span标签
                    child_spans = parent_span.find_elements(By.TAG_NAME, 'span')
                    
                    # 获取第五个子span标签的文本内容
                    exp = child_spans[2].text
                    #exp = ele.find_element(By.CSS_SELECTOR, '#app > div > div.post > div > div > div.j_result > div > div:nth-child(2) > div > div:nth-child(2) > div.j_joblist > div:nth-child(2) > div.el > p.info > span.d.at > span:nth-child(3)').text
                    # 学历
                    # 找到包含所有信息的父span标签
                    parent_span = ele.find_element(By.CSS_SELECTOR, 'span.d.at')
                    
                    # 在父span标签下找到所有的子span标签
                    child_spans = parent_span.find_elements(By.TAG_NAME, 'span')
                    
                    # 获取第五个子span标签的文本内容
                    edu = child_spans[4].text

                    #edu = ele.find_element(By.CSS_SELECTOR, '#app > div > div.post > div > div > div.j_result > div > div:nth-child(2) > div > div:nth-child(2) > div.j_joblist > div:nth-child(4) > div.el > p.info > span.d.at > span:nth-child(5)').text
                    # 公司的行业
                    industry = ele.find_element(By.CLASS_NAME, 'int.at').text
                    # 存储技能福利标签
                    skill_elements = ele.find_element(By.CLASS_NAME, 'tags').find_elements(By.TAG_NAME, 'span')
                    skills = [elem.get_attribute('title') for elem in skill_elements]
                    skills_str = ','.join(skills)
                    # 学历
                    #dt = ele.find_element(By.CSS_SELECTOR, '#app > div > div.post > div > div > div.j_result > div > div:nth-child(2) > div > div:nth-child(2) > div.j_joblist > div:nth-child(4) > div.el > p.info > span.d.at > span:nth-child(5)').text
                    # 来源
                    source = "51job"

                    # 插入数据库
                    insert_sql = "INSERT INTO job (jobname, company, city, sal, exp, edu, industry, skill, dt, source) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                    cursor.execute(insert_sql, (jobname, company, city_full, sal, exp, edu, industry, skills_str, "NULL", source))
                    con.commit()
                except Exception as e:
                    print(f"Error in inner loop: {e}")
            print("打印完毕，进入下一页")
            # 点击下一页
            driver.find_element(By.CLASS_NAME,'btn-next').click()
            sleep(5)
    except Exception as e:
        print(f"Error in outer loop: {e}")
    sleep(5)
print('打印完毕,正在关闭')
driver.quit()
cursor.close()
con.close()
