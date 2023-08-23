#`print()`函数是Python中的一个内置函数，用于输出信息到控制台。它是初学者学习和开发中经常使用的一个重要工具。

### 基本输出
# 使用`print()`函数最简单的用法是输出一个字符串。

# 基本输出
print("Hello, World!")

### 分隔符和结束符

# 你可以使用`sep`参数来定义输出中使用的分隔符，使用`end`参数来定义输出的结束符。
print("A", "B", "C", sep="-")   # 输出 "A-B-C"
print("First line", end="; ")   # 输出 "First line; " 并不换行
print("Second line")            # 输出 "Second line"


### 格式化输出
# Python提供了多种方式来格式化输出，如使用`f-string`或`format()`方法。
name = "Alice"
age = 25

# 使用f-string
print(f"{name} is {age} years old.")

# 使用format()方法
print("{} is {} years old.".format(name, age))


### 输出到文件
# 你还可以使用`print()`函数的`file`参数将输出重定向到文件。
with open('output.txt', 'w') as file:
    print("This will be written to a file.", file=file)