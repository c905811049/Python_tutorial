# 集合（Set）是Python中的一种数据结构，用于存储无序的、不重复的元素集合。
# 集合提供了许多有用的操作，如并集、交集、差集等。

### 10.1 创建集合
# 你可以使用大括号`{}`创建一个集合，或使用`set()`函数从其他可迭代对象创建集合。
primes = {2, 3, 5, 7, 11}
even_numbers = set([2, 4, 4, 6, 8]) # 重复元素将被忽略



### 10.2 添加和删除元素
# 你可以使用`add()`方法添加元素，使用`remove()`或`discard()`方法删除元素。
primes.add(13)         # 添加元素
primes.remove(2)       # 删除元素，如果元素不存在将抛出错误
primes.discard(3)      # 删除元素，如果元素不存在不会抛出错误



### 10.3 集合操作
# 集合提供了许多操作，如并集、交集、差集和对称差集。
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

union_set = a | b      # 或者 a.union(b)
intersection_set = a & b # 或者 a.intersection(b)
difference_set = a - b # 或者 a.difference(b)
symmetric_diff_set = a ^ b # 或者 a.symmetric_difference(b)



### 10.4 测试成员关系
# 你可以使用`in`关键字测试一个元素是否在集合中。
is_member = 5 in primes # 返回True


### 10.5 集合推导式
# 你可以使用集合推导式快速创建集合。
squares = {x**2 for x in range(5)}


### 10.6 集合的不可变版本
# `frozenset`是集合的不可变版本，可用作字典的键或其他集合的元素。
frozen = frozenset([1, 2, 3])


# 集合是非常有用的数据结构，尤其是当你需要处理无序、不重复的元素集合，并执行集合论操作时。

