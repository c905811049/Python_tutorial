# `for`循环是Python中用于迭代序列（例如列表、元组、字符串等）的一种控制结构。

### 5.1 基本for循环
# 通过`for`循环，你可以遍历任何序列的元素。
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)


### 5.2 使用range函数
# 使用`range()`函数，你可以生成一个数字序列并遍历它。
for i in range(5):  # 从0到4
    print(i)


### 5.3 遍历字符串
# 你还可以使用`for`循环遍历字符串的每个字符。
word = "Python"
for letter in word:
    print(letter)


### 5.4 使用enumerate函数
# `enumerate()`函数可用于同时获取元素及其索引。
for index, value in enumerate(numbers):
    print(f"Index {index}: {value}")


### 5.5 嵌套for循环
# 你可以在一个`for`循环内部使用另一个`for`循环，称为嵌套for循环。
for i in range(3):
    for j in range(3):
        print(i, j)


### 5.6 使用列表推导式
# 列表推导式是一种简洁的使用`for`循环创建列表的方法。
squares = [x**2 for x in range(5)]
print(squares)  # 输出 [0, 1, 4, 9, 16]