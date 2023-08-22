# 条件判断是编程中非常重要的一部分。在Python中，你可以使用if、elif（else if的缩写）和else关键字来进行条件判断。

# 4.1 基本if语句
### 使用if关键字，你可以执行特定代码块的条件。
x = 10
if x > 5:
    print("x is greater than 5")

# 4.2 if-else语句
### 你可以使用else关键字来定义当if条件不满足时执行的代码块。
if x > 20:
    print("x is greater than 20")
else:
    print("x is not greater than 20")

# 4.3 if-elif-else语句
### 使用elif关键字，你可以在多个条件之间进行选择。
if x > 20:
    print("x is greater than 20")
elif x > 10:
    print("x is greater than 10 but not greater than 20")
else:
    print("x is not greater than 10")

# 4.4 嵌套if语句
### 你还可以在一个if语句内部使用另一个if语句，这称为嵌套if语句。
if x > 5:
    print("x is greater than 5")
    if x > 10:
        print("x is also greater than 10")

# 4.5 使用逻辑运算符
###你还可以使用逻辑运算符and、or和not来组合多个条件。
y = 5
if x > 5 and y < 10:
    print("x is greater than 5 and y is less than 10")