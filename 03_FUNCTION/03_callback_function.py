# Python中也有回调函数的概念。回调函数是一种允许将一个函数作为参数传递给另一个函数的机制。
# 当某些条件满足或某些操作完成时，该函数将被调用，因此得名“回调”。

### 13.1 回调函数基础
# 在Python中，函数是一级对象，这意味着你可以将函数作为参数传递给另一个函数，并在其中调用它。
def callback():
    print("Callback function executed!")

def main_function(func):
    print("Main function executed!")
    func() # 调用回调函数

main_function(callback) # 输出Main function executed! 和 Callback function executed!



### 13.2 带参数的回调函数
# 回调函数还可以接受参数，并在主函数中传递。

def callback(name):
    print(f"Hello, {name}!")

def main_function(func, name):
    print("Main function executed!")
    func(name)

main_function(callback, "John")



### 13.3 Lambda作为回调
# 你可以使用Lambda函数作为回调，使代码更简洁。
main_function(lambda name: print(f"Hello, {name}!"), "John")



### 13.4 实际应用
# 回调函数在实际编程中非常有用，特别是在异步编程、事件驱动编程或执行耗时操作时。
# 例如，你可能有一个下载文件的函数，并希望在下载完成时通知用户：
def download_complete():
    print("Download complete!")

def download_file(url, callback):
    # 下载文件的代码
    print(f"Downloading from {url}...")
    # 下载完成后调用回调
    callback()

download_file("https://example.com/file.zip", download_complete)



### 13.5 回调的注意事项

# 虽然回调非常强大，但也要注意以下几点：
# - **可读性**：使用过多的回调可能会使代码难以阅读和维护。
# - **错误处理**：确保正确处理回调中的错误和异常。
# - **类型安全**：确保传递给回调的参数类型正确。

