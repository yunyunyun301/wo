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

### 10.2 文本数据的分类

结构化响应内容
* json字符串:可以使用re/json模块来提取特定数据
* xml字符串:可以使用re/lxml模块来提取特定数据

非结构化响应内容
* html字符串:可以使用re/bs4/lxml模块来提取特定数据

#### html 和 xml的区别
1. 语法不同：
   
   html是一种标记语言，使用标签来定义页面，侧重于显示

    xml侧重于数据存储和传输，使用标签来定义数据结构，没有预定义的标签，用户可以自定义标签。


### 10.3 json格式和python格式的互相转换

json格式是一种轻量级的数据交换格式，使用键值对的形式来表示数据，类似于Python中的字典和列表。

特点：
1. 易于阅读和编写：json格式使用简单的语法，易于阅读和编写。
2. 语言无关：json格式可以被多种编程语言支持，适用于不同语言之间的数据交换。
3. 支持复杂数据结构：json格式可以表示复杂的数据结构，如嵌套的对象和数组。

```py
import json

# json字符串转python对象
dic = {"name": "张三"}
dic2 = json.dumps(dic, ensure_ascii=False)  # 将python对象转换为json字符串
print(dic2)
# python对象转json字符串
dic3 = json.loads(dic2)
print(dic3)
print(type(dic3))
# json字符串转python对象

```
json模块的函数：
* json.dump():将python对象写入文件，参数包括python对象和文件对象。
* json.load():从文件中读取json数据并转换为python对象。
* json.dumps():将python对象转换为json字符串，参数包括python对象和ensure_ascii参数，默认值为True，表示将非ASCII字符转换为\uXXXX的形式，如果设置为False，则保留原有字符。
* json.loads():将json字符串转换为python对象，参数包括json字符串。
### 10.4 jsonpath模块
jsonpath模块是一个用于提取json数据的Python库，可以通过类似于XPath的语法来提取json数据中的特定部分。

#### 10.4.1 jsonpath模块的使用
1. 安装jsonpath模块：
```
pip install jsonpath
```
2. 语法规则


| jsonpath表达式 | 说明 |
| --- | --- |
| $ | 根节点 |
| . | 访问子节点 |
| [] | 访问数组元素 |
| * | 通配符，匹配所有元素 |
| [start:end] | 访问数组切片 |
| [?(expression)] | 过滤表达式，返回满足条件的元素 |
| .. | 递归搜索 |
| @ | 当前节点 |
| \| | 逻辑运算符，支持&&（与）、\|\|（或） |
| [index] | 访问数组中指定索引的元素 |
| [key] | 访问对象中指定键的值 |
| [key1,key2,...] | 访问对象中多个键的值 |
| [*] | 访问数组中所有元素 |
```json
# 示例json数据
json_data = {
    "store": {
        "book":[
            {"title": "Book 1", "price": 10},
            {"title": "Book 3","price": 30},
            {"title": "Book 2", "price": 20}
        ]
    }
}
```
|jsonpath|result|
|---|---|
|$.store.book[*].title|store下book数组中的所有元素的title|
|$.store..book|所有book元素|
|$.store.*|store下的所有元素|
|$.store..price|store下所有元素的price|
|$..book[2]|store下book数组中的第3个元素|
|$..book[(@.length-1)]\|$..book[-1:]|store下book数组中的最后一个元素|
|$..book[0,1]\|$..book[:2]|store下book数组中的前两个元素|
|$..book[?(@.price<20)]|store下book数组中price小于20的元素|
|$..book[?(@.title)]|store下book数组中title不为空的元素|
|$..*|store下的所有元素|


3. 使用jsonpath模块提取json数据：--通过jsonpath.jsonpath()函数来提取json数据中的特定部分，参数包括json数据和jsonpath表达式。
```py
import jsonpath

# 示例json数据
json_data = {
    "store": {
        "book":[
            {"title": "Book 1", "price": 10},
            {"title": "Book 3","price": 30},
            {"title": "Book 2", "price": 20}
        ]
    }
}

# 使用jsonpath提取数据
titles = jsonpath.jsonpath(json_data, '$.store.book[*].title')
print(titles)
prices = jsonpath.jsonpath(json_data, '$.store.book[?(@.price<20)].title')
print(prices)
```
### 10.5 Xpath模块

#### 10.5.1 Xpath模块的使用
1. 安装lxml模块：
```
pip install lxml
```
2. 导入模块

    1. 导入lxml.etree模块：用于解析HTML和XML文档。
    2. 利用etree.HTML()解析HTML文档，返回一个Element对象。
    3. 使用Element对象的xpath()方法来提取数据，参数是一个XPath表达式，返回一个列表，包含所有匹配的元素。
    
    另外一种：
    1. 导入lxml.html模块：用于解析HTML文档。
    2. 利用lxml.html.fromstring()解析HTML文档，返回一个Element对象。
    3. 使用Element对象的xpath()方法来提取数据，参数是一个XPath表达式，返回一个列表，包含所有匹配的元素。


3. XPath表达式的语法规则 [详见Xpath.md](Xpath.md)

4. 使用
```py
from lxml import etree
html = "获取的HTML字符串"
tree = etree.HTML(html)  # 解析HTML字符串，返回一个Element对象
response = tree.xpath('XPath表达式')  # 使用xpath()方法提取数据，返回一个列表
```

## 十一.反反爬

**反爬虫**是指网站采取的一系列措施来防止爬虫程序访问和获取数据的行为。常见的反爬虫措施包括：

1. IP封禁：通过监控访问频率和行为模式，封禁可疑的IP地址。
2. User-Agent检测：检查请求头中的User-Agent字段，识别和阻止爬虫程序。
3. 验证码：要求用户输入验证码来验证是否为人类访问。
4. 动态内容加载：通过JavaScript动态加载内容，增加爬取难度。
5. 反爬虫机制：如使用robots.txt文件来限制爬虫访问特定页面或目录。
6. 数据加密：对数据进行加密处理，增加爬取难度。
7. 频率限制：限制单位时间内的访问次数，防止过于频繁的请求。

**反反爬虫**是指爬虫程序采取的一系列措施来绕过网站的反爬虫机制，成功获取数据的行为。常见的反反爬虫措施包括：
1. user-agent伪装：通过修改请求头中的User-Agent字段，模拟正常用户的请求。
2. IP代理：使用代理服务器来隐藏真实IP地址，绕过IP封禁
3. referer伪装：通过修改请求头中的referer字段，模拟正常用户的访问来源。
4. cookie模拟：通过添加cookie信息来模拟登录状态，绕过验证码和登录限制。
5. 模拟浏览器行为：使用Selenium等工具模拟浏览器的行为，如点击、滚动等，绕过动态内容加载和反爬虫机制。

### 11.1 js加密

有些网站会对数据进行js加密，爬虫需要通过分析js代码来解密数据，才能获取到需要的数据。

### 11.2 hashlib模块
哈希值概念：哈希值是通过哈希算法对数据进行计算得到的一串固定长度的字符串，具有唯一性和不可逆性，可以用于数据的验证和安全存储。

hashlib模块是Python标准库中的一个模块，提供了多种哈希算法，如MD5、SHA1、SHA256等，可以用于生成数据的哈希值。

* MD5算法是一种常用的哈希算法，生成一个128位的哈希值，通常用于数据的完整性验证和密码存储。
* 加盐是指在原始数据的基础上添加一个随机字符串（盐），然后再进行哈希计算，以增加哈希值的复杂性和安全性，防止被暴力破解。

```py
import hashlib
st = 'hello world'
res=hashlib.new('md5',st.encode('utf-8'))
print(res.digest())#返回二进制数据
print(res.hexdigest())#返回十六进制数据

#md5使用
res2=hashlib.md5(st.encode())
print(res.digest())#返回二进制数据
print(res.hexdigest())#返回十六进制数据
    
```

### 11.3 base64模块
base64模块是Python标准库中的一个模块，提供了Base64编码和解码的功能，可以用于在网络传输中对数据进行编码和解码。

特点：

1. 可逆性：Base64编码是可逆的，可以通过解码还原原始数据。
2. 可读性：Base64编码后的数据由字母、数字和一些特殊

* 使用
```py
import base64
st = 'hello world'
# base64编码
a1=base64.b64encode(st.encode('utf-8'))
print(a1)  # 输出: b'aGVsbG8gd29ybGQ
# base64解码
a2=base64.b64decode(a1).decode('utf-8')
print(a2)  # 输出: hello world
```

## 十二.Ajax请求

Ajax（Asynchronous JavaScript and XML）是一种在不重新加载整个页面的情况下与服务器交换数据并更新部分网页内容的技术。它允许网页在后台与服务器进行通信，获取数据并动态更新页面内容，提高用户体验和交互性。

### 12.1 相关概念

* 异步：指在发送请求后，不需要等待服务器的响应，可以继续执行其他操作，服务器响应后再处理结果。
* 无刷新：指在页面不重新加载的情况下更新部分内容，避免了页面的闪烁和等待时间。
* XMLHttpRequest对象：是实现Ajax请求的核心对象，提供了发送HTTP请求和处理服务器响应的方法和属性。
## 十三. Selenium模块

Selenium是一个用于自动化测试和爬取动态网页的Python库，可以模拟浏览器的行为，如点击、滚动等，绕过动态内容加载和反爬虫机制。

### 13.1 Selenium模块的安装和使用

1. 安装浏览器驱动：根据使用的浏览器类型，下载对应的浏览器驱动，如ChromeDriver、GeckoDriver等，并将其路径添加到系统环境变量中。

或者下载对应浏览器的webdriver-manager库，自动管理浏览器驱动：
```
pip install webdriver-manager
```
2. 导包(以edge浏览器为例)
```py
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options #用于设置浏览器选项
```
3. 创建浏览器对象
```py
def setup():#创建浏览器对象的函数
    options = Options()
    options.add_argument("--no-sandbox")  #禁用沙盒模式（增加系统兼容性）
    options.add_argument("--headless")  #（可选）启用无头模式（不显示浏览器界面）
    options.add_experimental_option(name='detach', value=True)  #保持浏览器打开状态
    driver = webdriver.Edge(options=options)  #创建Edge浏览器对象
    driver.implicitly_wait(10)#设置隐形式等待时间，单位为秒，在查找元素时，如果元素没有立即出现，Selenium会等待一段时间，直到元素出现或者超时
    return driver
```

### 13.2 打开网页
```py
driver.get("https://www.baidu.com/")  #打开网页
driver.close()#关闭当前标签页
driver.quit()#关闭浏览器
```
#### 13.2.1 打开多个标签页
```py   
driver.get("https://www.baidu.com/")  #打开第一个网页
driver.execute_script("window.open('https://www.google.com/')")  #打开第二个网页
```
### 13.3 最大化最小化窗口、打开位置、窗口大小调整、截图、刷新
最大化和最小化窗口可以通过driver对象的maxmize_window()和minimize_window()方法来实现。
```py
driver.maximize_window()  #最大化窗口
driver.minimize_window()  #最小化窗口
```
打开位置可以通过driver对象的set_window_position()方法来实现，参数包括x和y坐标。
```py
driver.set_window_position(x=100, y=100)  # 设置窗口位置
```
窗口大小调整可以通过driver对象的set_window_size()方法来实现，参数包括宽度和高度。
```py
driver.set_window_size(width=800, height=600)  # 设置窗口大小
```
截图可以通过driver对象的save_screenshot()方法来实现，参数是保存截图的文件路径。

以及get_screenshot_as_file()方法，参数是保存截图的文件路径，返回值是一个布尔值，表示截图是否成功保存。
```py
driver.save_screenshot("screenshot.png")  # 保存截图
driver.get_screenshot_as_file("screenshot.png")  # 保存截图，返回值表示是否成功保存
```
刷新可以通过driver对象的refresh()方法来实现。
```py
driver.refresh()  # 刷新页面
```
### 13.4 元素定位
元素定位是指在网页中找到特定的元素，以便对其进行操作。
```py
from selenium.webdriver.common.by import By#导入By类，用于指定元素定位方式
```
通过find_element()和find_elements()方法来定位元素，参数包括By类和定位方式的值，返回一个WebElement对象，可以对其进行操作。

八种元素定位方式：
1. By.ID:通过元素的id属性来定位元素。
2. By.NAME:通过元素的name属性来定位元素。
3. By.CLASS_NAME:通过元素的class属性来定位元素。
4. By.TAG_NAME:通过元素的标签名来定位元素。
5. By.LINK_TEXT:通过元素的链接文本来定位元素。
6. By.PARTIAL_LINK_TEXT:通过元素的部分链接文本来定位元素。
7. By.CSS_SELECTOR:通过元素的CSS选择器来定位元素。
8. By.XPATH:通过元素的XPath表达式来定位元素。
#### 13.4.1 通过ID定位元素
```py
element = driver.find_element(By.ID, "element_id")  # 通过ID定位元素,找不到会抛出NoSuchElementException异常
```
#### 13.4.2 通过CLASS_NAME定位元素
class属性是HTML元素的一个属性，可以包含多个类名，用于定义元素的样式和行为。
比如：
```html
<div class="element_class element_class_name">...</div>
```
通过class属性定位元素
```py
element = driver.find_element(By.CLASS_NAME, "element_class")  # 通过class属性定位元素,找不到会抛出NoSuchElementException异常
#class属性不能包含空格，要使用下划线
elementlist= driver.find_elements(By.CLASS_NAME, "element_class_name")  #class有多个属性值时，使用find_elements()方法返回一个列表，包含所有匹配的元素，通过切片来获取特定的元素

```
#### 13.4.3 通过TAG_NAME定位元素
通过标签名定位元素
```py
element = driver.find_element(By.TAG_NAME, "input")  # 通过标签名定位元素,找不到会抛出NoSuchElementException异常
```
#### 13.4.4 通过LINK_TEXT定位元素
通过链接的文本精准定位元素
```py
element = driver.find_element(By.LINK_TEXT, "点击这里")  # 通过链接文本定位元素,找不到会抛出NoSuchElementException异常
```
#### 13.4.5 通过PARTIAL_LINK_TEXT定位元素
通过链接的部分文本模糊定位元素
```py
element = driver.find_element(By.PARTIAL_LINK_TEXT, "点击")  # 通过部分链接文本定位元素,找不到会抛出NoSuchElementException异常
```
#### 13.4.6 通过CSS_SELECTOR定位元素
通过CSS选择器定位元素

* 井号加id值，通过id定位元素

* 点号加class值，通过class定位元素

* 不加符号加标签名，通过标签名定位元素
* 属性选择器，通过元素的属性和值来定位元素

    [属性名=属性值]：匹配具有指定属性名和属性值的元素。
    
    [属性名*=属性值]：匹配具有指定属性名且属性值包含指定字符串的元素。
    
    [属性名^=属性值]：匹配具有指定属性名且属性值以指定字符串开头的元素。
    
    [属性名$=属性值]：匹配具有指定属性名且属性值以指定字符串结尾的元素。
* 通过selector组合定位元素
```py
element = driver.find_element(By.CSS_SELECTOR, "div.classname")  # 通过CSS选择器定位元素,找不到会抛出NoSuchElementException异常
```
#### 13.4.7 通过XPATH定位元素
通过XPath表达式定位元素
```py
element = driver.find_element(By.XPATH, "//div[@class='classname']")  # 通过XPath表达式定位元素,找不到会抛出NoSuchElementException异常
```
### 13.5 元素交互操作
元素交互操作是指对定位到的元素进行点击、输入文本、获取属性等操作。
#### 13.5.1 点击元素和清空输入框
```py
element.click()  # 点击元素
element.clear()  # 清空输入框
```
#### 13.5.2 输入文本
```py
element.send_keys("输入的文本")  # 输入文本
```
#### 13.5.3 获取元素属性
```py
attribute_value = element.get_attribute("属性名")  # 获取元素的属性值
```
#### 13.5.4 获取元素文本
```py
text = element.text  # 获取元素的文本内容
```
#### 13.5.5 获取元素标签名
```py
tag_name = element.tag_name  # 获取元素的标签名
```
#### 13.5.6 获取元素位置和大小
```py
location = element.location  # 获取元素的位置
size = element.size  # 获取元素的大小
```
#### 13.5.7 上传文件
```py
element.send_keys("文件路径")  # 上传文件，参数是要上传的文件的绝对路径
```
### 13.6 显式等待和隐式等待
等待是指在执行操作之前，等待某个条件满足后再继续执行，以确保操作的成功和稳定性。
#### 13.6.1 显式等待
显式等待是指在代码中明确指定等待的条件和时间，直到条件满足或超时后继续执行。

使用WebDriverWait类和expected_conditions模块来实现显式等待，参数包括浏览器对象、等待时间和等待条件。
```py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
wait = WebDriverWait(driver, 10)  # 创建WebDriverWait对象，等待时间为10秒
element = wait.until(EC.presence_of_element_located((By.ID, "element_id")))  # 等待元素出现，返回元素对象
```
#### 13.6.2 隐式等待
隐式等待是指在创建浏览器对象时设置一个全局的等待时间，在查找元素时，如果元素没有立即出现，浏览器会等待指定的时间，直到元素出现或超时后继续执行。

使用driver对象的implicitly_wait()方法来设置隐式等待时间，参数是等待的时间，单位为秒。
```py
driver.implicitly_wait(10)  # 设置隐式等待时间为10秒
element = driver.find_element(By.ID, "element_id")  # 查找元素，如果元素没有立即出现，浏览器会等待指定的时间，直到元素出现或超时后继续执行
``` 
### 13.7 获取句柄和切换标签页
句柄是指浏览器中每个窗口或标签页的唯一标识，可以通过句柄来切换不同的窗口或标签页。
```py
handle = driver.current_window_handle  # 获取当前窗口或标签页的句柄
handles = driver.window_handles  # 获取所有窗口或标签页的句柄
driver.switch_to.window(handles[0])  # 切换到指定的窗口或标签页
```
### 13.8 获取页面源代码和当前URL
```py
page_source = driver.page_source  # 获取页面源代码
current_url = driver.current_url  # 获取当前URL
```
### 13.9 警告框和弹窗处理
```py
from selenium.webdriver.common.alert import Alert
alert = Alert(driver)  # 创建Alert对象
alert.accept()  # 接受警告框
alert.dismiss()  # 取消警告框
driver.switch_to.alert.accept()  # 点击确定按钮
driver.switch_to.alert.dismiss()  # 点击取消按钮
print(alert.text)    #获取到警告框的文本内容
driver.switch_to.alert.send_keys("输入的文本")  #输入文本到警告框
```
### 13.10 iframe嵌套界面

iframe是指在一个HTML页面中嵌套另一个HTML页面的元素，可以通过切换到iframe来操作其中的元素。
```py
iframe = driver.find_element(By.TAG_NAME, "iframe")  # 定位到iframe元素
driver.switch_to.frame(iframe)  # 切换到iframe
driver.switch_to.default_content()  # 切换回主页面
```
### 13.11 网页前进和后退
```py
driver.back()  # 网页后退
driver.forward()  # 网页前进
```
### 13.12 网页滚动和鼠标操作
```py
from selenium.webdriver.common.action_chains import ActionChains
actions = ActionChains(driver)  # 创建ActionChains对象
actions.move_to_element(element).perform()  # 鼠标移动到指定元素
actions.click(element).perform()  # 点击指定元素
actions.double_click(element).perform()  # 双击指定元素
actions.context_click(element).perform()  # 右键点击指定元素
actions.move_by_offset(xoffset, yoffset).perform()  # 鼠标移动到指定偏移位置
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # 滚动到页面底部
driver.execute_script("window.scrollTo(0, 0);")  # 滚动到页面顶部
#滚动一定距离
driver.execute_script("window.scrollBy(0, 100);")  # 向下滚动100像素
```
## 十四.api接口
API接口是指应用程序编程接口，是一组定义了软件组件之间如何交互的规范和协议。API接口允许不同的软件系统之间进行通信和数据交换，使得开发者可以利用已有的功能和数据来构建新的应用程序。
### 14.1 API接口的使用
1. 了解API接口：首先需要了解API接口的功能、参数和返回值
2. 获取API接口的URL地址：通过API文档或开发者工具获取API接口的URL地址。
3. 发送请求：使用requests模块或其他HTTP库来发送请求，参数包括URL地址、请求方法、请求头和请求体等。
4. 解析响应：根据API接口的返回格式，使用相应的解析方法来提取需要的数据。
5. 错误处理：根据API接口的错误码和错误信息，进行相应的错误处理和异常捕获。
### 14.2 API接口的认证和授权
有些API接口需要进行认证和授权，才能访问和获取数据。常见的认证和授权方式包括：
1. API Key认证：通过在请求头或请求参数中添加API Key来进行认证，API Key是由API提供者生成的一串唯一的字符串，用于识别和授权用户。
2. OAuth认证：通过OAuth协议来进行认证和授权，OAuth是一种开放的授权协议，允许用户授权第三方应用访问其资源，而不需要暴露用户名和密码。
3. JWT认证：通过JSON Web Token来进行认证和授权，JWT是一种基于JSON的开放标准，用于在网络应用环境中传递声明，通常用于身份验证和信息交换。
### 14.3 API接口的速率限制
API接口的速率限制是指API提供者对API接口的访问频率进行限制，以防止滥用和保护服务器资源。
### 14.4 API接口的版本控制
API接口的版本控制是指在API接口的URL地址中添加版本号，以便在API接口发生变化时，保持向后兼容性，避免对现有应用程序造成影响。
### 14.5 API接口的文档和测试
API接口的文档是指对API接口的功能、参数、返回值和使用方法进行详细说明的文档，通常由API提供者编写和维护。API接口的测试是指对API接口进行功能测试、性能测试和安全测试等，以确保API接口的正确性、稳定性和安全性。
### 14.6 API接口的错误处理和异常捕获
API接口的错误处理是指根据API接口的错误码和错误信息，进行相应的错误处理和异常捕获，以提高应用程序的健壮性和用户体验。
### 14.7 例子 deepseekAPI接口的使用
deepseekAPI接口是一个提供了多种数据分析和处理功能的API接口，可以用于文本分析、图像识别、语音识别等领域。
```py
import os
from openai import OpenAI

client = OpenAI(
    api_key='',
    base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[{"role": "user", "content": "hello"}],
    stream=False
)

print(response.choices[0].message.content)
```
