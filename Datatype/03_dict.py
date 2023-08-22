# 字典是Python中的一种非常重要的数据结构，用于存储键值对。
# 字典中的每个元素都由一个键和一个值组成，你可以通过键来访问相应的值。

### 9.1 创建字典
# 你可以使用大括号`{}`来创建一个字典，并使用冒号`:`分隔键和值。
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}



### 9.2 访问字典元素
# 你可以使用键来访问字典中的值。
name = person["name"]  # 获取键为"name"的值



# 你还可以使用`get()`方法来访问字典中的值，并提供一个可选的默认值。
city = person.get("city", "Unknown") # 获取键为"city"的值，如果不存在则返回"Unknown"


### 9.3 修改和添加元素
# 你可以通过键来修改或添加字典中的元素。
person["age"] = 35      # 修改现有键的值
person["country"] = "USA" # 添加新键值对



### 9.4 删除元素

# 你可以使用`pop()`、`popitem()`和`del`关键字来删除字典中的元素。
person.pop("age")        # 删除键为"age"的元素
person.popitem()         # 随机删除并返回一个元素
del person["city"]       # 删除键为"city"的元素



### 9.5 遍历字典
# 你可以使用`keys()`、`values()`和`items()`方法来遍历字典的键、值或键值对。
for key in person.keys():
    print(key)

for value in person.values():
    print(value)

for key, value in person.items():
    print(key, value)


### 9.6 字典推导式
# 你可以使用字典推导式来快速创建字典。
squares = {x: x**2 for x in range(5)}


### 9.7 合并字典
# 你可以使用`update()`方法或`|`运算符（Python 3.9+）来合并两个字典。
person_details = {"height": 175, "weight": 70}
person.update(person_details) # 使用update方法


# 字典是非常灵活和强大的数据结构，用于表示和操作键值对集合。



