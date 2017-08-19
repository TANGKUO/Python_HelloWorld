'''
第一个示例：简单的网页爬虫
爬取豆瓣首页 
'''

import urllib.request
import re


#网址
url = "http://www.douban.com/"

#请求
request = urllib.request.Request(url)

#爬取结果
response = urllib.request.urlopen(request)

data = response.read()

#设置解码方式
data = data.decode('utf-8')

#打印结果
#print(data)


#正则过滤函数
def filter(html):
    print("正在进行正则表达式匹配...")
    re.sub('<br/>', '\n', html)#将网页中的换行符转换为\n
    regular = "[\u4e00-\u9fa5]+|\d+|\n|，|。|：|“|”"#正则表达式筛选出汉字和汉字标点符号
    doc = re.findall(regular,html)
    for i in range(170):
        doc.pop(0)
    for i in range(145):
        doc.pop()
    print("正则表达式匹配结束...")
    return doc

#写入txt文件函数
def txt(doc):  
    print("正在追加写入文档...")
    txt = ''.join(doc)
    f = open("D:/2017-git-javaSrc/python/重生之神级学霸.txt",'a')
    print("写入完毕...")
    print(txt)
    return txt

print(data)


#打印爬取网页的各类信息

print(type(response))
print(response.geturl())
print(response.info())
print(response.getcode())


html = filter(data)
txt(html)
print("程序结束!!!")
