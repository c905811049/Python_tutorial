# 列表是Python中的一种重要数据结构，它是一种有序的、可变的元素集合。

### 7.1 创建列表
# 你可以使用方括号`[]`来创建一个列表，并用逗号`,`分隔其中的元素。
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "cherry"]
mixed_list = [10, "hello", 3.14]


### 7.2 访问列表元素
# 你可以使用索引来访问列表中的元素。索引从0开始。
first_number = numbers[0]  # 获取第一个元素
third_fruit = fruits[2]   # 获取第三个元素


### 7.3 修改列表元素
# 由于列表是可变的，你可以修改其中的元素。
numbers[1] = 20  # 将第二个元素修改为20


### 7.4 添加和删除元素
# 你可以使用`append()`、`insert()`、`remove()`和`pop()`等方法来添加和删除元素。
numbers.append(6)     # 在末尾添加元素
numbers.insert(0, 0)  # 在指定位置插入元素
numbers.remove(3)     # 删除指定元素
numbers.pop(2)        # 删除指定位置的元素


### 7.5 列表切片
# 列表切片允许你访问列表的一部分。
sub_numbers = numbers[1:4]  # 获取索引1到3的元素


### 7.6 列表推导式
# 列表推导式是一种快速创建列表的方法。
squares = [x**2 for x in range(5)]  # 创建平方数列表



### 7.7 常用列表方法
# 列表还有许多其他有用的方法，如`sort()`、`reverse()`、`count()`等。
numbers.sort()    # 排序列表
numbers.reverse() # 反转列表
count_two = numbers.count(2) # 计算元素2的出现次数



