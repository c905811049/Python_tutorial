import time
# Python 的 `time` 模块提供了各种与时间有关的函数和方法。这个模块主要用于执行和管理与时间有关的任务，比如获取当前时间、格式化时间、延迟执行等。
### 1. 获取当前时间
#### 1.1 获取当前时间戳
# 使用 `time()` 函数可以获取自纪元（Epoch，1970年1月1日 00:00:00 UTC）以来的秒数。


current_time = time.time()
print("Current Time:", current_time)


#### 1.2 获取结构化时间
# 使用 `localtime()` 或 `gmtime()` 函数可以将时间戳转换为本地时间或格林威治时间。

local_time = time.localtime(current_time)
print("Local Time:", local_time)



### 2. 格式化时间
#### 2.1 时间戳转字符串

# 使用 `asctime()` 函数或 `strftime()` 函数可以将结构化时间转换为字符串。

time_string = time.asctime(local_time)
print("Time String:", time_string)

formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
print("Formatted Time:", formatted_time)


#### 2.2 字符串转时间戳
# 使用 `strptime()` 函数可以将时间字符串解析为结构化时间。

parsed_time = time.strptime("2022-01-01 12:34:56", "%Y-%m-%d %H:%M:%S")
print("Parsed Time:", parsed_time)


### 3. 延迟和暂停
#### 3.1 使用 `sleep()` 函数

# 该函数用于让程序暂停指定的秒数。

print("Start")
time.sleep(5)
print("End")

# 这将会先打印 "Start"，然后暂停 5 秒，最后打印 "End"。



### 4. CPU 时间
#### 4.1 `clock()`（不推荐）和 `process_time()`

# 这些函数用于获取 CPU 时间，通常用于性能测试和基准测试。

start = time.process_time()
# 进行一些计算
end = time.process_time()
elapsed_time = end - start



# 以上只是 `time` 模块的部分功能。该模块还提供了其他与时间有关的函数和方法，但这些应该足以覆盖大多数常见用例。

