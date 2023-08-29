# 函数是编程中的基本构建块之一，允许你将代码组织成可重用、可维护的块。在Python中，你可以使用`def`关键字定义函数。

### 11.1 定义函数
# 使用`def`关键字 followed by a function name 和参数列表来定义一个函数。
def greet(name):
    print(f"Hello, {name}!")


### 11.2 调用函数
# 通过函数名和括号`()`来调用函数，并将所需的参数传递给它。
greet("John")


### 11.3 返回值
# 使用`return`关键字从函数返回一个值。
def add(a, b):
    return a + b

result = add(3, 4) # result接收返回值7



### 11.4 默认参数
# 你可以为函数参数提供默认值，如果在调用函数时未提供该参数，则使用默认值。
def power(base, exponent=2):
    return base ** exponent

result = power(3) # result接收返回值9



### 11.5 关键字参数
# 在调用函数时，你可以通过参数名指定参数值。
result = power(exponent=3, base=2) # result接收返回值8



### 11.6 可变参数
# 使用`*args`和`**kwargs`来接收可变数量的位置参数和关键字参数。
def func(*args, **kwargs):
    print(args)   # 位置参数元组
    print(kwargs) # 关键字参数字典

func(1, 2, a=3, b=4)



### 11.7 Lambda函数
# Lambda函数是一种定义简单函数的快捷方式。

# 11.7 Lambda函数
multiply = lambda x, y: x * y
result = multiply(2, 3) # result接收返回值6


### 11.8 作用域
# 在函数中，变量有局部和全局作用域。局部变量仅在函数内部可见，而全局变量在整个程序中可见。
global_var = 10

def test_scope():
    local_var = 5
    print(global_var) # 可访问全局变量

# print(local_var) # 抛出错误，无法访问局部变量




### 11.9 文档字符串
# 你可以为函数添加文档字符串，以描述其功能和用法。
def square(x):
    """返回x的平方"""
    return x**2



# 函数是编程中的基本组成部分，允许你以模块化和可重用的方式组织代码。了解函数的这些特性和行为有助于编写清晰、有效的代码。
