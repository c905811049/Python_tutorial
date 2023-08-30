import pandas as pd
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# 替换这里的路径为您的Excel文件的实际路径
excel_path = 'C:\\Users\\90581\\Desktop\\PythonWorkplace\\Project\\Framework\\工作表 在 数据工程师题目(1).xlsx'

# 使用pandas读取Excel文件
df = pd.read_excel(excel_path)

# 显示前几行数据以确认读取成功
print(df.head())


# 定义一个函数来转换港股代码到A股代码
def convert_a_to_hk(a_code):
    a_code_str = str(a_code)
    
    # 定义转换规则
    convert_rules = {
        '688': '30',
        '300': '77',
        '301': '78',
        '00': '70',
        '60': '9'
    }
    
    # 根据A股代码的前两位或前三位来确定前缀
    for a_prefix, hk_prefix in convert_rules.items():
        if a_code_str.startswith(a_prefix):
            hk_code = hk_prefix + a_code_str[len(a_prefix):]
            return hk_code



# 测试函数
# hk_code_example = 300222
# a_code_example = convert_hk_to_a(hk_code_example)
# print(f"对应的A股代码是：{a_code_example}")


def select_date(driver, month, day):
    driver.find_element(By.ID, ("txtShareholdingDate")).click()
    parent_element = driver.find_element(By.CLASS_NAME, 'month')
    button = parent_element.find_element(By.CSS_SELECTOR, f'button[data-value="{month}"]')
    action = ActionChains(driver)
    action.move_to_element(button).perform()
    button.click()

    parent_element = driver.find_element(By.CLASS_NAME, 'day')
    button = parent_element.find_element(By.CSS_SELECTOR, f'button[data-value="{day}"]')
    action = ActionChains(driver)
    action.move_to_element(button).perform()
    button.click()

def input_stock_code(driver, stock_code):
    date_input = driver.find_element(By.ID,"txtStockCode")
    date_input.clear()
    date_input.send_keys(stock_code)


from time import sleep


def fetch_data(driver):
    search_button = driver.find_element(By.ID, "btnSearch")
    search_button.click()

    sleep(2)  # 等待页面刷新，可以优化为WebDriverWait
    stocks_tbody = driver.find_element(By.TAG_NAME, "tbody")
    stocks_rows = stocks_tbody.find_elements(By.TAG_NAME, "tr")

    holds_data = []
    for row in stocks_rows:
        try:
            tds = row.find_elements(By.TAG_NAME, "td")
            holds = tds[3].find_element(By.CLASS_NAME, 'mobile-list-body').text
            holds_data.append(int(holds.replace(',', '')))
        except Exception as e:
            print(f"Error in fetching data: {e}")

    return holds_data


# 初始化WebDriver和用于存储结果的字典
driver = webdriver.Edge()
result_dict = {}

# 打开目标网页
driver.get("https://www3.hkexnews.hk/sdw/search/searchsdw_c.aspx")

# 固定日期为2023-06-30
month = 5
day = 30

for index, row in df.iterrows():
    industry = row['行业']
    stock_code = row['A股股票票代码']

    # 转换A股代码到港股代码
    hk_stock_code = convert_a_to_hk(stock_code)

    # 初始化该行业的持股量为0（如果尚未初始化）
    if industry not in result_dict:
        result_dict[industry] = 0

    # 使用封装好的函数进行操作
    select_date(driver, month, day)
    input_stock_code(driver, hk_stock_code)  # 使用转换后的港股代码
    holds_data = fetch_data(driver)

    # 将获取到的持股量添加到该行业的汇总持股量中
    result_dict[industry] += sum(holds_data)

# 将汇总的持股量保存到Excel文件中
result_df = pd.DataFrame(list(result_dict.items()), columns=['行业', 'SUM(持股量)'])
result_df.to_excel('结果.xlsx', index=False)

