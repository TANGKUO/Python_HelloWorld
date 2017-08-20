#!/usr/bin/env python
# python+高德api实现自助找房
# coding: utf8
from bs4 import BeautifulSoup
from urlparse import urljoin
import requests
import csv
import html5lib

#同学们说一下  我想爬取一个网页  第一步干嘛呢
    #1、找到目标URL
    #2、分析html页面  获取html页面
    #3、进行所需内容的匹配
    #4、文件操作  写入csv文件

URL = "http://bj.ganji.com/fang1/o{page}p{price}/"
ADDR = "http://bj.ganji.com/"

if __name__ == '__main__':
    start_page = 1		# 开始页面
    end_page = 10		# 结束页面
    price = 7			# 价格
    with open("foo.csv", "wb") as f:		# 打开文件
        csv_writer = csv.writer(f, delimiter=',')	# 创建一个csv writer对象 传入一个文件句柄， 以逗号作为分隔符
        print("start...")
        while start_page < end_page:			# 判断当开始大于结束页面时停止爬虫
            start_page += 1				
            print("get: {0}".format(URL.format(page=start_page, price=price)))
            response = requests.get(URL.format(page=start_page, price=price)) 	# 调用requests模块的get方法，传入一个url地址
            html = BeautifulSoup(response.text, "html.parser")
            # 创建一个BeautifulSoup对象，第一个参数是抓取的html文本， 第二个是使用哪种解析器
            house_list = html.select(".f-list > .f-list-item > .f-list-item-wrap") # 获取房屋信息
            if not house_list:  # 没有则退
                break
            for house in house_list:								
                house_title = house.select(".title > a")[0].string.encode("utf8")		# 获取房源标题
                house_addr = house.select(".address > .area > a")[-1].string.encode("utf8")	# 获取房源地址
                house_price = house.select(".info > .price > .num")[0].string.encode("utf8")	# 获取房源价格
                house_url = urljoin(ADDR, house.select(".title > a")[0]["href"])		# 获取房源页面地址
                csv_writer.writerow([house_title, house_addr, house_price, house_url])		# 将房源信息写入csv文件中
        print("end")


#1.学习 requests模块的使用
#2.学习 beautifulsoup模块得简单用法
#3.学习 cvs模块得使用
#4.学习 高德地图api得使用


