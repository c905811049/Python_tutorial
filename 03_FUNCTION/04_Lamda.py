# Lambda函数，也称为**匿名函数**，是一种在Python中定义简单函数的快速方法。
# 与常规函数不同，Lambda函数是一行表达式，不使用标准的`def`和`return`关键字。
# 它们通常用于小型、一次性的操作，例如将函数作为参数传递给其他函数。

### 12.1 Lambda函数的语法
# Lambda函数的语法非常简洁。关键字`lambda`后跟参数，然后是冒号，再后面是一个表达式。
# lambda arguments: expression



### 12.2 使用Lambda函数
# 以下是一个使用Lambda函数来定义简单加法函数的示例。
add = lambda x, y: x + y
result = add(2, 3) # 结果为5



### 12.3 Lambda函数与常规函数
# 以下是一个使用常规函数和Lambda函数来定义相同功能的比较。
# **常规函数：**
def multiply(x, y):
    return x * y


# **Lambda函数：**
multiply = lambda x, y: x * y


### 12.4 Lambda函数和高阶函数
# Lambda函数通常与高阶函数（如`map()`、`filter()`和`reduce()`）一起使用。
# **使用`map()`应用函数到列表中的每个元素：**
numbers = [1, 2, 3, 4]
squares = map(lambda x: x**2, numbers)


# **使用`filter()`过滤列表中的元素：**
even_numbers = filter(lambda x: x % 2 == 0, numbers)



# **使用`reduce()`累积列表中的元素：**
from functools import reduce
total = reduce(lambda x, y: x + y, numbers)



### 12.5 Lambda函数的限制

# 虽然Lambda函数非常简洁，但它们也有限制：
#
# - Lambda函数只能包含一个表达式，不能包含复杂的逻辑。
# - Lambda函数不支持语句，如赋值和循环。
# - Lambda函数可能会降低代码的可读性，特别是如果过于复杂。
#
# 总的来说，Lambda函数是一种强大的工具，适合用于简单、一次性的操作。如果你发现自己正在编写复杂的Lambda函数，可能最好使用常规的`def`来定义函数，以保持代码的清晰和可维护性。



