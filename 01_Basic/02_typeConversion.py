# 在Python中，类型转换允许你将一种数据类型转换为另一种数据类型。以下是Python中常见的类型转换方法：

### 1. 转换为整数（int）
# 你可以使用`int()`函数将浮点数或符合整数格式的字符串转换为整数。
float_number = 5.9
integer_number = int(float_number)
string_number = "10"
integer_from_string = int(string_number)

print(integer_number)          # 输出 5
print(integer_from_string)     # 输出 10


### 2. 转换为浮点数（float）
# 使用`float()`函数，你可以将整数或符合浮点数格式的字符串转换为浮点数。
int_number = 5
float_number = float(int_number)
string_number = "5.7"
float_from_string = float(string_number)

print(float_number)          # 输出 5.0
print(float_from_string)     # 输出 5.7

### 3. 转换为字符串（str）
# 你可以使用`str()`函数将几乎任何类型的变量转换为字符串。
int_number = 10
float_number = 5.5
string_from_int = str(int_number)
string_from_float = str(float_number)

print(string_from_int)      # 输出 "10"
print(string_from_float)    # 输出 "5.5"

### 4. 转换为列表（list）
# 你可以使用`list()`函数将元组或字符串转换为列表。
tuple_number = (1, 2, 3)
list_from_tuple = list(tuple_number)
string_text = "Python"
list_from_string = list(string_text)

print(list_from_tuple)      # 输出 [1, 2, 3]
print(list_from_string)     # 输出 ['P', 'y', 't', 'h', 'o', 'n']

### 5. 转换为元组（tuple）
# 你可以使用`tuple()`函数将列表或字符串转换为元组。
list_number = [1, 2, 3]
tuple_from_list = tuple(list_number)

print(tuple_from_list)      # 输出 (1, 2, 3)


### 6. 转换为布尔值（bool）
# 你可以使用`bool()`函数将其他类型的值转换为布尔值。
# 通常，值为0、空字符串、空列表等的变量将转换为`False`，其他值将转换为`True`。
bool_from_zero = bool(0)
bool_from_non_zero = bool(5)

print(bool_from_zero)      # 输出 False
print(bool_from_non_zero)  # 输出 True

### 注意事项
#在转换类型时，确保转换是有意义的。例如，尝试将非数字字符串转换为整数将引发错误。
#在进行数学运算时，Python会自动进行某些类型转换。例如，将整数与浮点数相加会得到浮点数结果。