#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests

from bs4 import BeautifulSoup

url = 'http://zxzj.sheitc.gov.cn/xmgg.do'

r =  requests.get(url)

# r = requests.post('http://httpbin.org/post', data = {'key':'value'})
# >>> r = requests.put('http://httpbin.org/put', data = {'key':'value'})
# >>> r = requests.delete('http://httpbin.org/delete')
# >>> r = requests.head('http://httpbin.org/get')
# >>> r = requests.options('http://httpbin.org/get')

# >>> payload = {'key1': 'value1', 'key2': 'value2'}
# >>> r = requests.get("http://httpbin.org/get", params=payload)

soup = BeautifulSoup(r.text)

lis = soup.find('div', class_='newsbox')
for item in lis.find_all('li'):
	print(item.a.text, item.em.text) # item.a['href'],



