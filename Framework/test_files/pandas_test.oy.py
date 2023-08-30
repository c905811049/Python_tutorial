import pandas as pd
# 替换这里的路径为您的Excel文件的实际路径
excel_path = 'C:\\Users\\90581\\Desktop\\PythonWorkplace\\Project\\Framework\\工作表 在 数据工程师题目(1).xlsx'


# 读取整个Excel文件
df = pd.read_excel(excel_path)

# 选择名为'ColumnName'的列，并将其转换为列表
column_list = df['行业'].tolist()

# 打印列表
print(column_list)

# 初始化一个空列表来存储行数据
rows_list = []

# 遍历DataFrame的每一行
for index, row in df.iterrows():
    # 将行数据转换为字典
    row_dict = row.to_dict()

    # 将字典添加到列表中
    rows_list.append(row_dict)

# 打印列表以进行检查
print(rows_list)