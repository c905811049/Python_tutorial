'''
# 审题
- 收集用户手机号(验证)
- 收集用户密码(验证)
- 确认密码
- 收集用户邮箱(验证)
- 打印注册信息并提示成功

# 思路：
## 用函数封装

### 主函数
主函数作为主入口，负责执行子函数并处理数据，以及打印提示内容。
  - while循环，可以让用户选择什么时候退出输入数据
  - 执行功能函数
  - 保存信息
  - 打印提示内容

### 注册手机号函数
  - 手机号校验规则
  - 返回用户填写的值
  
### 注册用户密码函数
  - 用户密码校验规则
  - 返回用户填写的值
  
### 确认密码函数
  - 传入之前用户填写的密码数据
  - input让用户再次输入信息
  - 对比二者是否相等
  
### 注册邮箱函数
  - 邮箱信息验证
  - 返回用户填写的值
'''


# 获取用户手机信息函数
def get_phone_number():
    while True:
        phone_number = input("请输入手机号（11位，以数字1开头）：")
        # 校验规则,如果错误则提示错误并让用户再次输入，如果正确则返回正确结果
        if len(phone_number) == 11 and phone_number.isdigit() and phone_number[0] == "1":
            return phone_number
        print("手机号输入错误，请重新输入。")

# 获取用户密码函数
def get_password():
    while True:
        password = input("请输入密码（长度6-20之间）：")
        # 校验规则,如果错误则提示错误并让用户再次输入，如果正确则返回正确结果
        if 6 <= len(password) <= 20:
            return password
        print("密码长度不符合要求，请重新输入。")

# 用户密码校验函数
# 参数 password:传入一个值来验证用户之后的填写两者是否相等
def confirm_password(password):
    while True:
        confirm_password = input("请确认密码：")
        # 校验规则,如果错误则提示错误并让用户再次输入，如果正确则返回正确结果
        if confirm_password == password:
            return confirm_password
        print("密码不一致，请重新输入。")

# 获取用户邮箱地址函数
def get_email():
    while True:
        email = input("请输入邮箱（至少包含@，并以.com或.cn结尾）：")
        # 校验规则,如果错误则提示错误并让用户再次输入，如果正确则返回正确结果
        # 判断@字段是否存在于用户输入的内容中，并且用字符串的endswith来判断结尾是否为.com和cn
        # 这只是一个粗略的判断，如果要严谨可以使用正则表达式
        if "@" in email and (email.endswith(".com") or email.endswith(".cn")):
            return email
        print("邮箱格式错误，请重新输入。")

# 主函数
def main():
    # 创建一个用户数组，用于保存记录
    users = []
    while True:
        # 创建字典，用于保存用户输入的信息
        user_info = {}
        user_info['phone_number'] = get_phone_number()
        user_info['password'] = get_password()
        confirm_password(user_info['password'])
        user_info['email'] = get_email()
        
        # 将字典插入到数组中
        users.append(user_info)

        # 打印用户输入的信息方便查看
        print("\n注册成功！以下是您的注册信息：")
        print(f"手机号：{user_info['phone_number']}")
        print(f"密码：{user_info['password']}")
        print(f"邮箱：{user_info['email']}")

        # 执行逻辑：询问用户是否继续添加新的信息
        another_user = input("是否要注册另一个用户？ (y/n): ")
        # 检测用户输入，如果为why则退出循环，即终止信息填写
        if another_user.lower() != 'y':
            break
    
    # 打印出用户填写的所有信息，用于验证
    print("\n所有注册用户：")
    for user in users:
        print(f"手机号：{user['phone_number']}, 邮箱：{user['email']}")

# 执行main函数
main()