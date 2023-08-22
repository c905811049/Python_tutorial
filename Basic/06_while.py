# `while`循环是Python中的另一种重要循环结构。与`for`循环不同，`while`循环会一直执行，直到指定的条件不再满足。


### 6.1 基本while循环
# `while`循环会重复执行代码块，直到条件表达式的值为`False`。
count = 0
while count < 5:
    print(count)
    count += 1

### 6.2 使用else语句
# 你可以使用`else`子句在`while`循环条件不再满足时执行一段代码。
while count < 10:
    print(count)
    count += 1
else:
    print("Count is no longer less than 10")

### 6.3 使用break语句
# break`语句可以用来立即退出`while`循环。
while True:
    print(count)
    count += 1
    if count > 15:
        break


### 6.4 使用continue语句
# continue`语句可以用来跳过当前迭代，并继续下一次循环。
while count < 20:
    count += 1
    if count % 2 == 0:  # 如果count是偶数
        continue
    print(count)


### 6.5 无限循环
# 如果`while`循环的条件始终为`True`，则会创建无限循环。


# 6.5无限循环（警告：这将导致无限循环，请谨慎运行）
# while True:
#     print("This will print indefinitely.")
