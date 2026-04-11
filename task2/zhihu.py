from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options #用于设置浏览器选项
from selenium.webdriver.common.by import By#导入By类，用于指定元素定位方式
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import requests
import random
def setup():#创建浏览器对象的函数
    
    cookies = '_xsrf=w1TU0VukQ6bfH05mQab2m8ZMxjhcRcSu; _zap=1eb67a22-83ac-42c0-b5f5-fd848753eab1; d_c0=8wJUbG8h8hqPTvAF64qL6y6oHaReXqHCVY8=|1755705708; q_c1=fa01527ae2684088bbcef15e78baadee|1774795752000|1774795752000; r_cap_id=\'MjU5ZDZmMTY2NzdiNDQ2YjgwMjgzOThiNDlmMjAzNzg=|1774795752|cac35468291278b58ccbce0309c557a77678b2aa\'; cap_id="NmFkMzljMmJmOGYzNDZmNTk3YjU3YTljYjA4NzVkNGQ=|1774795752|53cd9d59e8ae3ee9f394a7a5c80aef2a01cc09e5"; l_cap_id="NWMwODMzOGFjNTcxNGYxMmE2OWRjZjEwMjMzYWMyNTE=|1774795752|f15034348df887e1af0eb0f3607113ea1afcba50"; captcha_session_v2=2|1:0|10:1774795764|18:captcha_session_v2|88:S0Z4cmszd1hQNXV2QlFsMUF5ajk0dWZiZ3lxTjNEak15dkZZRTVXbEd5a2NiQXAvVlpYNUR5RXVOalJVOHhEUw==|996820a91e749aa518043d049c56055ecebe4b55608284ca0ba40baf5c3af8ab; gdxidpyhxdE=XEw8grMasXqTcw%2B9zDSS%2BEj0ZoXSH%2FLlCywqqu9kTvaZdhU4%5COWE%5CuLkm%2BRCMYCB7D0yJZBoP16vqQh2hMAttus%2F5ZzQUS9Ned232mv71JduXzUofSujKa%2BRseaxWpCPXaf%2FfZAUGNqiHLmnRVbJM%2F46KzRC2vr%5CQ4fGliQS6Qs3SBL%2F%3A1774796666356; z_c0=2|1:0|10:1774795783|4:z_c0|92:Mi4xOFZ6dm93QUFBQUR6QWxSc2J5SHlHaVlBQUFCZ0FsVk5Cb3EyYWdDZlBaSThsemFQa3hRdkFRUXVjc3dvb0VyVzZB|6c55d1ad0f290b2f152c5e81cba97a58c985d59ad0529b7a1a9e2e528d874373; __utmv=51854390.100--|2=registration_date=20260209=1^3=entry_date=20260209=1; __zse_ck=005_wtHlZIAe1vWds66OGBpd1cJBamALUAA=stud3vP7mtsT=CS4PAP77HhoCKCYHGjN8S0g=jIfpxVpWPxVlJINIBImPL73HAIOc1CmRBInufsJjh0IAGdgVoCLnyhWW4Tt-l+L3HbPUkqZ4D/I19i4efbdf0lgJBv4yDLRqr4L36c72Ykw3UzdoPa+e1Om/zDvsGFDN9ljQ/YpiQ4r3o/8GqenfENmmMrXspYKVDexgJ9OGhmXgjB6ESyl0qL8GSGyQ; __utma=51854390.1159773009.1774795754.1775744836.1775749787.3; __utmz=51854390.1775749787.3.3.utmcsr=github.com|utmccn=(referral)|utmcmd=referral|utmcct=/west2-online/learn-AI/blob/main/tasks(2026)/foundation/task2.md; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1774795764,1774883890,1775744878,1775835088; HMACCOUNT=AF2FA6B51F344AF7; BEC=1eb0fb512bb6053f407f0a7771f545e9; unlock_ticket=FzWUObvE0BsmAAAAYAJVTW8i2WlyW0o0-wt3DKBwkC8n3DJ0rV9zUA==; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1775836008'
        
    options = Options()
    options.add_argument("--no-sandbox")  #禁用沙盒模式（增加系统兼容性）
    options.add_experimental_option(name='detach', value=True)  #保持浏览器打开状态
    options.add_experimental_option("excludeSwitches", ["enable-automation"])#去除浏览器自动化控制的提示
    options.add_experimental_option('useAutomationExtension', False)#禁用浏览器自动化扩展
    options.add_argument('user_agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36')#设置浏览器的User-Agent字符串，模拟正常用户访问
    driver = webdriver.Edge(service=Service('msedgedriver.exe'),options=options)  #创建Edge浏览器对象
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
        Object.defineProperty(navigator, 'webdriver', {
            get: () => undefined
        });
    """
})#通过执行CDP命令，修改浏览器的navigator.webdriver属性，使其返回undefined，进一步隐藏自动化控制的痕迹
    driver.implicitly_wait(10)#设置隐形式等待时间，单位为秒，在查找元素时，如果元素没有立即出现，Selenium会等待一段时间，直到元素出现或者超时
    driver.get("https://www.zhihu.com/")#打开知乎首页
    for i in cookies.split("; "):#将cookie字符串按照"; "分割成一个个cookie，然后遍历每个cookie
        name, value = i.split("=", 1)
        driver.add_cookie({"name": name, "value": value})#将cookie字符串分割成键值对，并使用add_cookie方法将每个cookie添加到浏览器中
    driver.refresh()#刷新页面，使添加的cookie生效
    return driver
def switch_to_new_window(driver, x, oldurl=None):#切换到新打开的窗口或标签页的函数
    handles = list(driver.window_handles)  # 获取所有窗口或标签页的句柄
    driver.switch_to.window(handles[x])  # 切换到指定窗口或标签页
    print(f"从{oldurl}切换到{driver.current_url}")#打印切换前后的URL
driver = setup()#调用setup函数创建浏览器对象
wait = WebDriverWait(driver, 10)  # 创建WebDriverWait对象，等待时间为10秒
driver.get("https://www.zhihu.com/topics")#打开知乎话题广场

time.sleep(random.randint(2, 5))#等待页面加载完成
n=0
while n<=10:
    topics=driver.find_elements(By.XPATH,value=f"//div[@class='zh-general-list clearfix']//strong")
    topics[n].click()#点击话题进入话题详情页
    n+=1
    switch_to_new_window(driver,-1,driver.current_url)#切换到新打开的窗口或标签页
    time.sleep(random.randint(1,3))#等待页面加载完成
    driver.find_element(By.PARTIAL_LINK_TEXT,value="等待回答").click()

    time.sleep(random.randint(1,3))#等待页面加载完成
    try:
        driver.find_element(By.XPATH,value="//div[@class='List']//a[@href]").click()#点击第一个问题进入问题详情页
    except:
        print("系统繁忙，请稍后再试！直接关闭当前窗口，继续爬取下一个话题！")
        driver.close()
        switch_to_new_window(driver,0)#切换到第一个标签页,即话题广场
        time.sleep(random.randint(2, 5))#等待页面加载完成
        continue
    switch_to_new_window(driver,-1,driver.current_url)#切换到新打开的窗口或标签页
    title=driver.find_element(By.XPATH,value="//*[@id='root']/div/main/div/div/div[1]/div[2]/div/div[1]/div[1]/h1").text
    try:
        driver.find_element(By.XPATH,value="//div[@class='QuestionHeader-main']//button").click()#点击显示全部按钮，展开问题描述内容
        question=driver.find_element(By.XPATH,value="//div[@class='QuestionHeader-main']//span[@id='content']").text#获取问题的描述内容
    except:
        print("未能找到显示全部按钮！")
        question = "没有找到问题描述！"

    # driver.find_element(By.CLASS_NAME, value="QuestionHeader-Comment").click()#点击问题描述下的评论按钮，展开评论区  
    # time.sleep(random.randint(1,3))#等待页面加载完成
    # commit=driver.find_elements(By.CLASS_NAME, value="CommentContent_css-tgyln6")
    # print(commit[0].text)#打印第一条评论的内容
    # driver.find_element(By.XPATH,value="/html/body/div[5]/div/div/div[2]/button/svg/path").click()
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")#将页面滚动到最底部，以加载更多内容
        content=driver.find_elements(By.ID,value="content")
        if len(content)>10:#如果页面上已经加载了内容，就跳出循环
            break
    with open("zhihu.csv","a",encoding="utf-8") as f:#将问题内容保存到zhihu.cvs文件中
        f.write(f"问题标题: {title}\n\n")#先写入问题标题
        f.write(f"问题描述: {question}\n\n")#写入问题描述
        num=0
        for i in content[1:]:
            f.write(i.text+"\n")
            num+=1
            f.write(f"-------------------第{num}条回答-------------------\n")#写入每条回答的内容，并在每条回答后面写入回答的序号
            
    driver.close()#关闭当前窗口或标签页
    switch_to_new_window(driver,-1)
    driver.close()#关闭当前窗口或标签页
    switch_to_new_window(driver,0)#切换到第一个标签页,即话题广场
    time.sleep(random.randint(2, 5))#等待页面加载完成
driver.quit()#关闭浏览器对象，结束程序运行