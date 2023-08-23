# 1.1变量
### 变量定义和赋值

# 在Python中，变量不需要显式声明类型。当你给变量赋值时，Python会自动确定变量的类型。


name = "Alice"  # 字符串类型
age = 25  # 整数类型
height = 1.68  # 浮点数类型

### 变量命名规则

# 变量名称可以包含字母、数字和下划线，但不能以数字开头。

my_name = "Bob"
age1 = 30

### 变量类型

# 可以使用`type()`函数来查看变量的类型。
print(type(name))  # <class 'str'>
print(type(age))  # <class 'int'>
print(type(height))  # <class 'float'>

### 动态类型

# Python是一种动态类型语言，这意味着你可以更改变量的类型。例如：
x = 5
print(type(x))  # <class 'int'>
x = "hello"
print(type(x))  # <class 'str'>

### 多变量赋值

# 可以一次为多个变量赋值。
a, b, c = 5, 3.2, "Hello"

# 或者为多个变量赋相同的值：
x = y = z = "same"
