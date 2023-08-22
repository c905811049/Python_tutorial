# 元组是Python中的另一种序列数据类型，与列表非常相似，
# 但有一个关键区别：元组是不可变的。这意味着一旦创建了元组，就不能更改、添加或删除其中的元素。

### 8.1 创建元组
# 你可以使用圆括号`()`来创建一个元组，并用逗号`,`分隔其中的元素。
numbers_tuple = (1, 2, 3, 4, 5)
fruits_tuple = ("apple", "banana", "cherry")
single_element_tuple = (42,)  # 单个元素的元组需要后面的逗号



### 8.2 访问元组元素
# 你可以使用索引来访问元组中的元素，与列表的索引方式相同。
first_number = numbers_tuple[0]  # 获取第一个元素
third_fruit = fruits_tuple[2]    # 获取第三个元素


### 8.3 元组是不可变的
# 尝试修改元组中的元素会导致TypeError。

# numbers_tuple[1] = 20  # 这将导致错误



### 8.4 元组解包
# 你可以将元组中的元素解包到变量中。
a, b, c = (1, 2, 3)



### 8.5 元组与列表之间的转换
# 你可以使用`tuple()`和`list()`函数在元组和列表之间进行转换。
list_from_tuple = list(numbers_tuple)
tuple_from_list = tuple(list_from_tuple)



### 8.6 元组的常用方法
# 由于元组是不可变的，所以它的方法较少。常用的方法包括`count()`和`index()`。
count_twos = numbers_tuple.count(2)  # 计算元素2的出现次数
index_three = numbers_tuple.index(3) # 找到元素3的索引位置



# 元组通常用于表示不应更改的数据集合，或者用于确保数据的完整性和一致性。

