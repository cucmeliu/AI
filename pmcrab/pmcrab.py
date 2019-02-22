#!/usr/bin/python
# -*- coding: UTF-8 -*-


import requests
from bs4 import BeautifulSoup
import re


# 1.urllib.request模块是用来打开和读取URLs的；
# 2.urllib.error模块包含一些有urllib.request产生的错误，可以使用try进行捕捉处理；
# 3.urllib.parse模块包含了一些解析URLs的方法；
# 4.urllib.robotparser模块用来解析robots.txt文本文件.它提供了一个单独的RobotFileParser类，通过该类提供的can_fetch()方法测试爬虫是否可以下载一个页面。


def get_path(province):
	return province

def get_jiangsu_fagaiwei():
	target = 'http://fzggw.jiangsu.gov.cn/col/col282/index.html'
	resp = request.urlopen(target)
	html = resp.read()

	bf = BeautifulSoup(html, 'lxml')

	return ''

def get_jiangsu_info():
	path = get_path('jiangsu')

	get_jiangsu_fagaiwei()

def get_sh_fgw_zxxxgk():
	url = 'http://www.shdrc.gov.cn/info/iList.jsp?cat_id=10199&q=1'
	print('\n =========== 上海 发改委 最新公开 ', url)

	r =  requests.get(url)
	soup = BeautifulSoup(r.text, 'lxml')

	lis = soup.find('div', class_='xwzx_list')
	for item in lis.find_all('li'):
		print(item.a.text, item.span.text) # item.a['href'],

def get_sh_jxw_zxzj():
	url = 'http://zxzj.sheitc.gov.cn/xmgg.do'
	print('\n =========== 上海 经信委 专项资金 ', url)

	r =  requests.get(url)
	soup = BeautifulSoup(r.text, 'lxml')

	lis = soup.find('div', class_='newsbox')
	for item in lis.find_all('li'):
		print(item.a.text.strip(), item.em.text) # item.a['href'],

def get_sh_jxw_zxzj_all():
	

def get_sh_kewei_zxgk():
	
	url = 'http://www.stcsm.gov.cn/info/iList.jsp?node_id=GKxxgk&cat_id=10094'
	print(' =========== 上海 科委 最新公开 ', url)
	r =  requests.get(url)
	soup = BeautifulSoup(r.text, 'lxml')
	print(soup.prettify())

	lis = soup.find('div', class_='lis')
	print('===',type(lis))
	for item in lis.find_all('li'):
		print(item.a.text, item.span.text) # item.a['href'],


def main():
	# - get_sh_kewei_zxgk
	get_sh_jxw_zxzj()
	get_sh_fgw_zxxxgk()


if __name__ =="__main__":
	main()
