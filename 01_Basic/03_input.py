### 1.2 输入

#### 获取用户输入

#可以使用`input()`函数来获取用户输入的字符串。以下是如何使用`input()`函数的示例：

### 获取用户输入
# 使用`input()`函数获取用户输入的字符串
user_name = input("请输入你的姓名: ")
print(f"你好, {user_name}!")

### 拼接字符串
# 你可以使用`+`运算符来拼接字符串。以下是如何拼接字符串的示例：
char1 = 'lu'
char2 = 'jk'

char3 = char1 + char2
print(char3)

# 使用占位符
name = '1'
out = '你的名字是%s' % name

print(out)

# 使用f-string
name = '1'
out = f'你的名字是{name}'
print(out)

# 使用format
name = '1'
out = '你的名字是{}'.format(name)

#### 转换输入类型
#你可能需要将输入转换为特定类型，例如整数或浮点数。以下是如何将用户输入的字符串转换为整数的示例：

# 转换输入类型
# 使用`int()`函数将用户输入的字符串转换为整数
user_age = int(input("请输入你的年龄: "))
if user_age >= 18:
    print("你是个成年人.")
else:
    print("你是未成年.")