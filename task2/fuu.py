#使用到的第三方库：requests、lxml、selenium、webdriver_manager
import requests
from lxml import html
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
import time
import re
options = EdgeOptions()
options.add_argument("--headless=new")
driver = webdriver.Edge(service=EdgeService(), options=options)#创建Edge浏览器实例
def extract_attachment_times(url):# 提取附件下载次数的函数
        
              
    driver.get(url)
    tree=html.fromstring(driver.page_source)
    attachmenttimes=tree.xpath("//li/span[@id]/text()")#提取附件下载次数  
    for i in range(5):
        attachmenttimes.append(0)    #防止越界崩溃
    return attachmenttimes

try:         
    url = 'https://jwch.fzu.edu.cn/jxtz/1.htm'#首页链接
    count=1
    getcount=0
    altime=0
    with open('fzu.csv','w+',encoding='utf-8') as f:
        while count<=209: #爬取500条数据  
            print("正在爬取第"+str(count)+"页")
            starttime=time.time()
            res=requests.get(url)                                      #获取网页内容
            tree = html.fromstring(res.content.decode('utf-8'))
            urlpool=tree.xpath("//ul[@class='list-gl']//a/@href")      #提取链接                        
            usedurlpool=["https://jwch.fzu.edu.cn/"+res.group() for i in urlpool if (res:=re.search(r'info/\d+/\d+(\.)htm|content.+',i))]  #筛选链接  
            Notifierpool=tree.xpath("//ul[@class='list-gl']//li/text()")#提取通知人文本      
            partern=r'质量办|教学运行|电教中心|实践科|综合科|计划科|教研教改|教材中心|铜盘校区管理科'  #定义正则表达式 
            cleaned_Notifierpool=[ res.group() for i in Notifierpool if (res:=re.search(partern, i))]    #提取通知人
            lastpool=dict(zip(usedurlpool, cleaned_Notifierpool)) #将链接和通知人对应起来
            for URL,notifier in lastpool.items():
                response=requests.get(URL)
                if response!=None:           
                    tree = html.fromstring(response.content.decode('utf-8'))
                    titles=tree.xpath("//h4/text()")                           #提取标题
                    attachment=tree.xpath("//li/a[@href]/text()")              #提取附件标题
                    attachmenturl=tree.xpath("//li/a/@href")                   #提取附件链接
                    if attachmenturl!=[]:
                        attachmenttimes=extract_attachment_times(URL)          #提取附件下载次数    
                        print("正在提取附件下载次数")
                    else :attachmenttimes=[]
                    date=tree.xpath("//span[@class='xl_sj_icon']/text()")      #提取发布时间
                    signature=[tree.xpath(f"string(//div[@class='v_news_content']//p[last()-{i}])") for i in range(15) ]   #提取落款
                    Notifier=[i.strip() for i in signature if re.search(r'教学质量监控与评估中心|教务处|教学运行科|注册中心', i)]    #提取通知人
                    if Notifier==[]:#如果在//div[@class='v_news_content']//p[last()-{i}])中没有找到通知人，则在//div[@class='v_news_content']/p[last()-{i}]中寻找
                        signature=[tree.xpath(f"string(//div[@class='v_news_content']/p[last()-{i}])") for i in range(15) ]   #提取落款
                        Notifier=[i.strip() for i in signature if re.search(r'教学质量监控与评估中心|教务处|教学运行科|注册中心', i)]    #提取通知人
                        if Notifier==[]:
                            Notifier=['未找到通知人']
                    getcount+=1
                    f.write(f'--------------第{getcount}条--------------\n')#储存数据
                    f.write('来源:'+str(notifier)+'\n')            
                    f.write(titles[0] + '\n')
                    f.write(date[0] + '\n')
                    f.write('详情链接: '+URL+'\n')
                    f.write('通知人:'+str(Notifier[0]) + '\n')
                    for i in range(len(attachment)):
                        f.write('附件:'+attachment[i]+'\n')
                        f.write('下载链接:'+"https://jwch.fzu.edu.cn"+attachmenturl[i]+'\n')
                        f.write('下载次数:'+str(attachmenttimes[i])+'\n')
                        
            endtime=time.time() 
            altime+=(endtime-starttime)
            print("耗时",f"{(endtime-starttime):.6f}","秒")
            count+=1        
            url='https://jwch.fzu.edu.cn/jxtz'+f"/{count}.htm"  #获取下一页链接，翻页
            
            
finally:
            print("总耗时",f"{altime:.6f}","秒")
            driver.quit()      





    
# try:         
#     response=requests.get('https://jwch.fzu.edu.cn/info/1036/13988.htm')
#     tree = html.fromstring(response.content.decode('utf-8'))
#     titles=tree.xpath("//h4/text()")                           #提取标题
#     attachment=tree.xpath("//li/a[@href]/text()")              #提取附件标题
#     print(attachment)
#     attachmenturl=tree.xpath("//li/a/@href")                   #提取附件链接
#     print(attachmenturl)
#     if attachmenturl!=[]:
#         attachmenttimes=extract_attachment_times('https://jwch.fzu.edu.cn/info/1036/13988.htm')#提取附件下载次数    
#         print(attachmenttimes)
#     date=tree.xpath("//span[@class='xl_sj_icon']/text()")      #提取发布时间
#     signature=[tree.xpath(f"string(//div[@class='v_news_content']/p[last()-{i}])") for i in range(15) ]   #提取落款
#     for i in range(15):
#         signature.append(tree.xpath(f"string(//div[@class='v_news_content']//p[last()-{i}])") )   #提取落款最后一行
    
#     Notifier=[i.strip() for i in signature if re.search(r'教学质量监控与评估中心|教务处|教学运行科', str(i))]    #提取通知人
    
# finally:
#     driver.quit()
