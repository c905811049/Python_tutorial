import csv
import random

# 预定义一些可能的名字
names = ["Alice", "Bob", "Charlie", "David", "Eva"]

# 打开一个新的 CSV 文件
with open('students.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    
    # 写入表头
    writer.writerow(["Name", "Student ID", "Age", "Gender"])
    
    # 生成 10 万名学生
    for i in range(100000):
        name = random.choice(names)  # 随机选择一个名字
        student_id = f"STU{i:05}"  # 生成学号
        age = random.randint(18, 25)  # 随机生成年龄
        gender = random.choice(["Male", "Female"])  # 随机选择性别
        
        # 写入一行学生数据
        writer.writerow([name, student_id, age, gender])
