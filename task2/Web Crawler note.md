# 网络爬虫

## 一.网络请求

网络爬虫的第一步是发送网络请求，获取网页的HTML内容。

### 1.请求过程
1. 请求网址  -- request URL
2. 请求方法  -- request method
3. 请求头    -- request headers
4. 请求体    -- request body

* F12查看网络请求

## 二.爬虫的概念与分类

### 2.1爬虫的概念

模拟浏览器，发送请求，获取数据的程序

### 2.2爬虫的作用
1. 数据采集
2. 软件测试
3. 网络安全
4. 抢票
5. web漏洞扫描

### 2.3爬虫的分类
1. 通用爬虫：适用于各种网站，能够抓取大量数据
2. 聚焦爬虫：针对特定网站或特定类型的数据进行抓取

根据获取数据的目的：
1. 功能性爬虫：用于特定功能，如搜索引擎爬虫
2. 数据增量爬虫：用于数据采集和分析

## 三.爬虫的工作流程
流程：对URL发送网络请求-->获取响应-->解析数据-->存储数据

爬虫的工作流程可以分为以下几个步骤：
1. 确认目标URL:www.baidu.com
2. 发送网络请求:获取特定服务器的响应
3. 提取数据：从响应中提取特定数据
4. 保存数据：将提取的数据保存到数据库或文件中

### 3.1 URL管理
1. URL队列：存储待爬取的URL
2. URL去重：避免重复爬取同一URL
3. URL优先级：根据URL的重要性和相关性进行排序

### 3.2 robots协议

robots协议是一种用于规范爬虫行为的协议，网站管理员可以通过robots.txt文件来指定哪些页面可以被爬虫访问，哪些页面不能被爬虫访问。

## 四.网络通信

### 4.1 网络通信的基本流程
url-->DNS服务器->返回IP地址-->TCP连接-->发送HTTP请求-->服务器处理请求-->返回HTTP响应-->关闭TCP连接

一个请求只能获取一个数据包，爬虫需要不断发送请求来获取更多的URL和数据。
### 4.2 HTTP协议
HTTP协议是客户端与服务器之间通信的协议，爬虫通过HTTP协议与服务器进行交互。
* http协议：超文本传输协议，是一种应用层协议，基于TCP/IP协议进行通信。默认端口号为80。
* 超文本：不局限于文本，可以包含图片、视频、音频等多媒体内容。
* https协议：安全的超文本传输协议，是http协议的安全版本，使用SSL/TLS加密传输数据。默认端口号为443。
* ssl/tls协议：安全套接层/传输层安全协议，是一种加密协议，用于保护数据在网络中的传输安全。\

### 4.3 http请求/响应的步骤：
1. 客户端连接到web服务器
2. 客户端发送http请求
3. 服务器接收请求并回应
4. 释放tcp连接
5. 客户端解析HTML内容
6. 客户端关闭连接

### 4.4 请求头
请求头是HTTP请求中的一部分，包含了客户端发送给服务器的各种信息，如浏览器类型、语言、编码等。

#### 4.4.1 请求方式：get 和 post

* get请求：将参数附加在URL后面，适用于**获取**数据，参数可见，长度有限制。
* post请求：将参数放在请求体中，适用于**提交**数据，参数不可见，没有长度限制。

#### 4.4.2 常见响应状态码
* 200 OK：请求成功
* 302 ：跳转
* 303：浏览器对post请求重定向至新的URL
* 307：浏览器对get请求重定向至新的URL
* 403: 资源被禁止访问
* 404: 资源未找到
* 500: 服务器内部错误
* 503: 服务器暂时无法处理请求

#### 4.4.3 常见请求头
* User-Agent: 浏览器类型和版本信息,用于模拟正常用户
* cookie: 存储用户的会话信息,用于保持**登录状态**
* referer: 来源页面的URL,用于防止**盗链**

抓包得到的响应内容才是判断依据，elements中的源码是渲染之后的源码，不能作为判断依据。

## 五 requests模块
作用：发送HTTP请求，获取响应内容，处理HTTP请求和响应的细节。
### 5.1 requests模块的基本使用
安装requests模块：
```
pip install requests
```
实例：
```python
import requests
#找到目标url
url="https://www.baidu.com/"
#发送请求
response = requests.get(url)
#打印响应
print(response.text)  
#有乱码,requests会自动寻求一种解码方式去解码
print(response.content.decode('utf-8'))  
#指定解码方式去解码 
```
爬取图片：
```python   
import requests
#找到目标url
url="目标图片的URL地址"
#发送请求
response = requests.get(url)
#保存响应
with open(r"crawler/image.jpg", "wb") as f:
    f.write(response.content)
```
### 5.2 requests模块的其他属性

requests.txt和requests.content的区别：
* requests.text: 返回响应内容的字符串形式，requests会自动根据响应头中的编码信息进行解码，默认使用utf-8编码。
* requests.content: 返回响应内容的字节形式，不进行解码，适用于处理二进制数据，如图片、视频等。可以通过response.content.decode('编码方式')来手动解码成字符串形式。

其他属性：
* status_code: 返回响应的状态码，如200、404等。
* headers: 返回响应的头部信息。
* cookies: 返回响应中的cookie信息。
* request.headers: 返回请求的头部信息。
```py
import requests
#找到目标url
url="https://www.baidu.com/"
#发送请求
response = requests.get(url)
#保存响应
print(response.status_code)  # 输出响应的状态码
print(response.headers)      # 输出响应的头部信息
print(response.request.headers)  # 输出请求的头部信息
print(response.cookies)      # 输出响应中的cookie信息
```

### 5.3 用户代理

请求头中的User-Agent字段用于标识客户端的浏览器类型和版本信息，服务器可以根据这个信息来判断请求来自哪个浏览器，从而返回适合该浏览器的内容。在爬虫中，设置User-Agent可以模拟正常用户的请求，避免被服务器识别为爬虫而拒绝访问。
#### 5.3.1 构建User-Agent
可以通过以下方式构建User-Agent：
1. 模拟常见浏览器的User-Agent，如Chrome、Firefox、Safari等。
2. 使用第三方库，如fake_useragent，来生成随机的User-Agent。
#### 5.3.2 设置User-Agent
在requests模块中，可以通过headers参数来设置User-Agent：
```python
import requests
url="https://www.baidu.com/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0"
}
response = requests.get(url, headers=headers)
#headers参数可以模拟浏览器的请求头，避免被服务器拒绝访问,模拟浏览器发送请求
print(response.content.decode('utf-8'))  
#输出响应的内容
print(len(response.content))
#输出响应的内容长度
#添加User-Agent请求头，模拟浏览器发送请求，避免被服务器拒绝访问
```

#### 5.3.3 user-agent池

为了避免被服务器识别为爬虫，可以使用一个User-Agent池，随机选择一个User-Agent来发送请求。

* user-agent池是一个包含多个User-Agent字符串的列表，可以从网上找到常见浏览器的User-Agent字符串，或者使用第三方库来生成随机的User-Agent。

1. 构建User-Agent池：创建一个包含多个User-Agent字符串的列表。
```py
import random
import requests
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0","Mozilla/5.0 (iPhone; CPU iPhone OS 18_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.5 Mobile/15E148","Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Mobile Safari/537.36 Edg/146.0.0.0"]
url="https://www.baidu.com/"
headers = {
    "User-Agent": random.choice(user_agents)
}       #随机选择一个User-Agent
```
2. 使用**第三方库**生成随机User-Agent：可以使用fake_useragent库来生成随机的User-Agent。
```py
import requests
from fake_useragent import UserAgent
url="https://www.baidu.com/"
headers = {
    "User-Agent": UserAgent().random
}       #随机选择一个User-Agent
```

### 5.4 浏览器发送请求原理
浏览器会向服务器发送请求，包括了请求方法,url,http协议

1. 构建请求
2. 查找缓存(返回资源的副本并结束请求)
3. DNS解析(将域名转换为IP地址)
4. 等待tcp队列
5. 建立TCP连接
6. 发送HTTP请求
7. 服务器处理请求

## 六 url传参
URL传参是指在URL中附加参数来传递数据给服务器，常见的传参方式有两种：查询参数和路径参数。

字符串被当作url提交时会被自动编码，特殊字符会被转换为%加上对应的ASCII码的十六进制表示。

quote:将字符串进行URL编码，特殊字符会被转换为%加上对应的ASCII码的十六进制表示。
unquote:将URL编码的字符串进行解码，%加上对应的ASCII码的十六进制表示会被转换回原来的字符。



例如：
```py
import requests
from urllib.parse import quote
url = "https://www.baidu.com/s?wd=%E7%A7%91%E6%AF%94&rsv_spt=1&rsv_iqid=0xb225dfcf0032e8c4&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_dl=tb&rsv_enter=1&rsv_sug3=7&rsv_sug1=5&rsv_sug7=100&rsv_btype=i&inputT=1347&rsv_sug4=4424" #wd=%E7%A7%91%E6%AF%94 是"科比"的URL编码形式

print(quote("科比"))  # 输出: %E7%A7%91%E6%AF%94
print(unquote("%E7%A7%91%E6%AF%94"))  # 输出: 科比
```
### 6.1 发送带参数的请求
通过params参数来发送带参数的请求，params参数可以是一个字典或者一个字符串，requests会自动将其转换为URL编码的形式。

```py
import requests
url = "https://www.baidu.com/s"
params = {
    "wd": "科比"
}
response = requests.get(url, params=params)
``` 

案例：网易云音乐 图片 歌曲 mv爬取
```py
import requests
#获取图片
url = "https://p5.music.126.net/obj/wonDlsKUwrLClGjCm8Kx/79009113855/5277/2cca/2f70/122549495c2686da275b9d012146773e.jpg?imageView&quality=89"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0"}
res=requests.get(url, headers=headers)
with open("1.jpg", "wb") as f:
    f.write(res.content)
#获取歌曲
url="https://m704.music.126.net/20260321002237/34b52345aa88c2c96c5ffaf1c8982189/jdyyaac/obj/w5rDlsOJwrLDjj7CmsOj/79011592465/8b35/eaa5/017f/e66a74e30005be387f14861b0e6a4246.m4a?vuutv=QHHflWYni8cPEZ8sCAe9ABCeG7eqTnnfSNw9o1u/xddfo6sXpAm0hAR4ePYMTRXwpOSKZIVz2TLzEnMSawZSyr0hrL8pszCEudXblbxNpOk=&authSecret=0000019d0bf76a7a03dd0a3b2090098e&cdntag=bWFyaz1vc193ZWIscXVhbGl0eV9leGhpZ2g"
res2=requests.get(url)
with open("我会等.m4a", "wb") as f:
    f.write(res2.content)
#获取mv
url="https://vodkgeyttp8.vod.126.net/cloudmusic/ICAiMDAwIGAwICAgISIiJA==/mv/375130/fab51440788fca8cdfcf2726b7328947.mp4?wsSecret=c2d84c411479a50cd0ed7f3aeeb251b6&wsTime=1774022572"
res3=requests.get(url)
with open("mv.mp4", "wb") as f:
    f.write(res3.content)
```
百度贴吧翻页
```py
import requests
import random
word=input("请输入贴吧关键词：")
page=int(input("请输入页数："))
url="https://tieba.baidu.com/f?"
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0","Mozilla/5.0 (iPhone; CPU iPhone OS 18_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.5 Mobile/15E148","Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Mobile Safari/537.36 Edg/146.0.0.0"]
for i in range(page):
    params = {
        "kw": word,
        "pn": i*50
    }
    response = requests.get(url, params=params, headers={"User-Agent": random.choice(user_agents)})
    with open(f"{word}_page_{i+1}.html", "w", encoding="utf-8") as f:
        f.write(response.text)
```
改写为面向对象
```py
class TiebaCrawler:
    def __init__(self):
        self.url = "https://tieba.baidu.com/f?"
        self.user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0","Mozilla/5.0 (iPhone; CPU iPhone OS 18_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.5 Mobile/15E148","Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Mobile Safari/537.36 Edg/146.0.0.0"]
    def send(self,params):
        response = requests.get(self.url, params=params, headers={"User-Agent": random.choice(self.user_agents)})
        return response.text
    def save(self,content,word,page):
        with open(f"{word}_page_{page}.html", "w",encoding="utf-8") as f:
            f.write(content)
    def run(self):
        word=input("请输入贴吧关键词：")
        page=int(input("请输入页数："))
        for i in range(page):
            params = {
                "kw": word,
                "pn": i*50
            }
            content=self.send(params)
            self.save(content,word,i+1)
```

## 七.post请求

post请求是HTTP协议中的一种请求方法，主要用于向服务器提交数据。与get请求不同，post请求将数据放在请求体中，而不是URL中，因此适用于提交大量数据或敏感数据。

### 7.1 使用场景

1. 提交表单数据：如登录、注册、评论等功能。
2. 上传文件：如图片、文档等。
3. 提交JSON数据：如API接口调用等。

### 7.2 发送post请求
在requests模块中，可以通过requests.post()方法来发送post请求，参数包括url、data、json等。

requests.post(url,data)方法的参数：
* url: 请求的URL地址
* data:接收一个字典

```py
import requests
url = "URL地址"
data = {
    "key1": "value1",
    "key2": "value2"
}
response = requests.post(url, data=data)
```

### 7.3 添加cookies模拟登录状态

在发送post请求时，可以通过headers参数添加cookie信息来模拟登录状态。cookie是服务器发送给客户端的一段数据，客户端会在后续的请求中携带这段数据，以保持登录状态。

使用方法：
1. 找到登录后的cookie信息，可以通过浏览器的开发者工具查看。
2. 将cookie信息添加到请求头中，发送post请求。

案例：--模拟豆瓣登录
```py
import requests
url = "https://accounts.douban.com/j/mobile/login/basic"
data = {
    "name": "你的用户名",
    "password": "你的密码",
    "remember": "true"
}
response = requests.post(url, data=data)
print(response.json())  # 输出响应的JSON数据
```

### 7.4 session对象保持登录状态

requests模块提供了session对象，可以在多个请求之间保持登录状态，自动处理cookie信息。
使用方法：
1. 创建一个session对象。
2. 使用session对象发送登录请求，保持登录状态。
```py
import requests
session = requests.Session()#实例化session对象
url = "URL"
data = {
    "name": "你的用户名",
    "password": "你的密码",
    "remember": "true"
}
response = session.post(url, data=data)  # 使用session对象发送登录请求
session.get("登录后需要访问的URL")  # 使用session对象发送其他请求，保持登录状态
```

### 7.5 cookie池
为了避免被服务器识别为爬虫，可以使用一个cookie池，随机选择一个cookie来发送请求。
1. 构建cookie池：创建一个包含多个cookie信息的列表。
2. 使用cookie池：在发送请求时，随机选择一个cookie信息添加到请求头中。
```py
import requests
import random
cookie_pool = [
    "cookie1",
    "cookie2",
    "cookie3"
]
res = requests.get("URL", headers={"cookie": random.choice(cookie_pool)})  # 随机选择一个cookie信息添加到请求头中
```

cookie与session对象的区别：
* cookie数据保存在客户端，session对象保存在服务器端。
* cookie安全性较低，容易被篡改，session对象安全性较高。
* cookie适用于存储少量数据，session对象适用于存储大量数据。 

## 八.代理

代理是指在网络请求中，通过一个中间服务器来转发请求和响应，以隐藏真实的IP地址，绕过IP限制，提升爬虫的匿名性和安全性。

代理ip是一个ip，指向一个代理服务器，爬虫通过这个代理服务器发送请求，服务器看到的请求来源是代理服务器的ip地址，而不是爬虫的真实ip地址。

### 8.1 正向代理

为客户端做代理，使服务器不清楚客户端的真实ip

### 8.2 反向代理
为服务器做代理，使客户端不清楚服务器的真实ip
### 8.3 代理的分类
1.   透明代理：服务器可以看到客户端的真实IP地址，适用于需要记录客户端信息的场景。
2.   匿名代理：服务器无法看到客户端的真实IP地址，但可以看到使用了代理，适用于需要隐藏客户端信息的场景。
3.   高匿代理：服务器既看不到客户端的真实IP地址，也看不到客户端使用了代理，适用于需要最高级别匿名性的场景。

### 8.4 使用代理发送请求
proxies的使用方法
1. 构建proxies字典：包含http和https协议的代理服务器地址。
2. 在发送请求时，使用proxies参数来指定代理服务器。
```py
proxies = {
    "http": "http://代理服务器地址",
    "https": "https://代理服务器地址"
}
response = requests.get("URL", proxies=proxies)
```
代理ip无效时，会使用本机ip发送请求，导致被服务器识别为爬虫而拒绝访问，因此需要定期更新代理ip池，确保代理ip的有效性和匿名性。

### 8.5 代理ip测试

```py
import requests

url="https://tool.lu/ip/"#ip地址查询接口

headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0'}
proxies={
    "https":"67.43.236.18:10873"
}
res=requests.get(url,headers=headers,proxies=proxies)
with open("ip.html","w",encoding="utf-8") as f:
    f.write(res.text)
```

## 九.retrying模块和timeout

### 9.1 介绍

retrying模块是一个用于实现重试机制的Python库，可以在请求失败时自动重试，增加爬虫的稳定性和可靠性。

timeout参数是requests模块中的一个参数，用于设置请求的超时时间，防止请求长时间无响应导致爬虫卡死。

### 9.2 retrying模块的使用
1. 安装retrying模块：
```
pip install retrying
```
2. 使用retrying模块实现重试机制：--在需要重试的函数上使用@retry装饰器，指定重试的条件和次数。
```py
from retrying import retry
import requests

@retry(stop_max_attempt_number=3) #重试3次
def test():
    print("test")
    url="https://www.zhihu.com/"
    response = requests.get(url)
try:
    test()
except Exception as e:
    print("请求失败，错误信息：", e)
```
### 9.3 timeout参数的使用
在发送请求时，可以通过timeout参数来设置请求的超时时间，单位为秒。
```py
from retrying import retry
import requests

@retry(stop_max_attempt_number=3) #重试3次
def test():
    print("test")
    url="https://www.baidus.com/"#故意写错URL，模拟请求失败的情况
    response = requests.get(url, timeout=5)
try:
    test()
except Exception as e:
    print("请求失败，错误信息：", e)
```

## 十.数据提取

### 10.1 异步加载
定义：异步加载是指网页中的某些数据不是在初始HTML中直接返回的，而是通过JavaScript代码在页面加载后动态获取的。这些数据通常通过AJAX请求从服务器获取，并在页面上进行渲染。

