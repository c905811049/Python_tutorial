'''`requests` 是一个非常流行的 Python 库，用于发送 HTTP 请求和处理 HTTP 响应。它是一个封装了 Python 标准库中的 `http.client`、`urllib` 等模块的高级接口，使得发送 HTTP 请求变得非常简单。

### 安装

  可以在本地环境中运行以下命令来安装：

    ```Shell
pip install requests
```


### 基础使用

  下面是一些基础的使用方法：

  #### 发送 GET 请求

    ```Python
import requests

response = requests.get('https://www.example.com')
print(response.text)
```


#### 发送 POST 请求

```Python
payload = {'key1': 'value1', 'key2': 'value2'}
response = requests.post('https://www.example.com/post', data=payload)
print(response.text)
```


### 请求参数

你可以轻松地添加 URL 参数、请求头、表单数据、JSON 数据等。

#### URL 参数

```Python
payload = {'key1': 'value1', 'key2': 'value2'}
response = requests.get('https://www.example.com/get', params=payload)
```


#### 自定义请求头

```Python
headers = {'user-agent': 'my-app'}
response = requests.get('https://www.example.com', headers=headers)
```


### 响应处理

`requests` 模块也提供了丰富的响应处理选项。

#### 响应状态码

```Python
print(response.status_code)
```


#### 响应头

```Python
print(response.headers)
```


#### 响应内容

```Python
print(response.text)
```


或者以 JSON 格式解析响应：

```Python
json_response = response.json()
```


### 高级功能

#### 超时设置

```Python
response = requests.get('https://www.example.com', timeout=5)
```


#### 会话对象

如果你需要跨多个请求保持某些参数（例如 Cookie），你可以使用会话对象。

```Python
with requests.Session() as session:
    session.get('https://www.example.com/login')
    response = session.get('https://www.example.com/dashboard')
```


这只是 `requests` 库的冰山一角。这个库还提供了很多其他高级功能，如代理支持、SSL 验证、自动重定向、流式请求等。
'''
