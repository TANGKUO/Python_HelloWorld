import urllib.request
import re

 
#定义网页抓取函数
def source(url):
    print("正在分析url...")
    source = urllib.request.urlopen(url)
    html = source.read()
    html = html.decode("utf - 8")
    print("网页抓取完毕...")
    return html
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
    f = open("重生之神级学霸.txt",'a')
    print("写入完毕...")
    print(txt)
    return txt
url = input("请输入需要爬的网址:\n")
S = source(url)
html = filter(S)
txt(html)
print("程序结束!!!")