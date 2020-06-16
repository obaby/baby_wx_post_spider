# coding: utf-8

import json
import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup(open('F:/PyCharmProjects\spider/135.html', 'r'), "html.parser")

#The Dormouse's story

nameList = soup.find_all("div",{"class":"rich_media_content "})

for name in nameList:
    print('\n')
    print(name.get_text())


book_list_img = soup.find_all('img')

for book_one in book_list_img:
    book_img_url = book_one.get('data-before-oversubscription-url') # src
    img_data_src = book_one.get('data-src')
    print(book_img_url)
    print(img_data_src)
    #request.urlretrieve(book_img_url, 'E:\python_spider_fild\%s.jpg' %x)
    #x += 1