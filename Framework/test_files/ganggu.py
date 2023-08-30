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
def convert_hk_to_a(hk_code):
    hk_prefix = str(hk_code)[:2]  # 提取港股代码的前两位
    hk_suffix = str(hk_code)[2:]  # 提取港股代码的后面部分

    # 定义转换规则
    convert_rules = {
        '30': '688',
        '77': '300',
        '78': '301',
        '70': '00',
        '71': '00',
        '72': '00',
        '73': '00',
        '9': '60'
    }

    # 找到对应的A股前缀
    a_prefix = convert_rules.get(hk_prefix, '')

    # 组合成完整的A股代码
    a_code = a_prefix + hk_suffix
    return a_code


# 测试函数
# hk_code_example = 300222
# a_code_example = convert_hk_to_a(hk_code_example)
# print(f"对应的A股代码是：{a_code_example}")

# 初始化Edge驱动
driver = webdriver.Edge()

# 打开目标网页
driver.get("https://www3.hkexnews.hk/sdw/search/searchsdw_c.aspx")


driver.find_element(By.ID,("txtShareholdingDate")).click()


# 先定位到父元素
parent_element = driver.find_element(By.CLASS_NAME, 'month')

# 从父元素中进一步查找目标按钮
button = parent_element.find_element(By.CSS_SELECTOR, 'button[data-value="5"]')

action = ActionChains(driver)
action.move_to_element(button).perform()
button.click()


# 先定位到父元素
parent_element = driver.find_element(By.CLASS_NAME, 'day')

# 从父元素中进一步查找目标按钮
button = parent_element.find_element(By.CSS_SELECTOR, 'button[data-value="30"]')

# 点击按钮
action = ActionChains(driver)
action.move_to_element(button).perform()
button.click()


# 定位到日期输入框并输入日期（这里假设输入框的id是'date_input'）
date_input = driver.find_element(By.ID,"txtStockCode")
date_input.clear()
date_input.send_keys("90519")

# 点击搜寻按钮（这里假设按钮的id是'search_button'）
search_button = driver.find_element(By.ID,"btnSearch")
search_button.click()

# 等待页面刷新
sleep(2)  

# 找到包含股票数据的tbody
stocks_tbody = driver.find_element(By.TAG_NAME,"tbody")

# 找到tbody下的所有tr
stocks_rows = stocks_tbody.find_elements(By.TAG_NAME, "tr")

# 存储持股量
holds_data = []

# 遍历每一个tr
for row in stocks_rows:
    try:
        # 找到该行下的所有td
        tds = row.find_elements(By.TAG_NAME, "td")
        
        # 持股量
        holds = tds[3].find_element(By.CLASS_NAME,'mobile-list-body').text

        # 将股票代码和持股量添加到列表中
        holds_data.append({
            'industry': '医药',
            'holds': int(holds.replace(',', ''))  # 移除逗号并转换为整数
        })
        
        print(f"添加了持股量： {holds}")

    except Exception as e:
        print(f"Error in outer loop: {e}")

# 输出保存的数据以进行检查
print(holds_data)


# 将数据转换为DataFrame
df_holds = pd.DataFrame(holds_data)

# 按照行业进行持股量的汇总
result = df_holds.groupby('industry')['holds'].sum().reset_index()


result.columns = ['行业', 'SUM(持股量)']

# 显示汇总结果
print(result)

result.to_excel("结果.xlsx", index=False)
# # 输出找到的元素以进行检查
# print(holding_data)
print('holding_data')
# 关闭浏览器
driver.quit()
