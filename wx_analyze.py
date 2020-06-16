# coding: utf-8

import requests
from requests.exceptions import *
from bs4 import BeautifulSoup
import json
import sys


def qsprint(dict_or_list):
    print(u'[*] DATA:' + (json.dumps(dict_or_list, encoding="UTF-8", ensure_ascii=False)))


def get_wxpost_html_content(post_link):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',
    }  # 替换成自己的cookie
    status = 0
    try:
        r = requests.get(
            post_link,
            headers=headers)
    except Exception as e:
        print(e)
        status = 1
    if status == 1:
        return ''
    return r.text


def get_wxpost_text_content(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    nameList = soup.find_all("div", {"class": "rich_media_content "})
    dest_string = ''
    for name in nameList:
        dest_string = dest_string + name
    print(soup.head.string)
    # The Dormouse's story
    print(soup.title.string)

    return dest_string


def get_wxpost_text_html_content(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    nameList = soup.find_all("div", {"class": "rich_media_content "})
    dest_string = ''
    for name in nameList:
        dest_string = name
    print(dest_string)
    return dest_string


def get_wxpost_all_p(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    all_ps = soup.find_all("p")
    ps = []

    for p in all_ps:
        ps.append(p.get_text())
    # 获取段落内span的内容

    return ps


def get_wxpost_text_title_content(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    nameList = soup.find_all("div", {"class": "rich_media_content "})
    dest_string = ''
    for name in nameList:
        # print('\n')
        # print(name.get_text())
        dest_string = dest_string + name.get_text()
    head = soup.head.string
    # The Dormouse's story
    title = soup.title.string

    return title, dest_string


def get_title(html_content):
    bs = BeautifulSoup(html_content, "html.parser")
    title = bs.find('h2', id='activity-name').get_text()
    return title


def get_wxpost_img_links(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    imgs = soup.find_all('img')
    img_links = []
    for img in imgs:
        img_url = img_data_src = src = ''
        try:
            img_url = img.get('data-before-oversubscription-url')  # src
        except:
            pass
        try:
            img_data_src = img.get('data-src')  # data-src
        except:
            pass
        try:
            src = imgs.get('src')
        except:
            pass
        if img_url and len(img_url) > 8:
            img_links.append(img_url)
        if img_data_src and len(img_data_src) > 8:
            img_links.append(img_data_src)
        # if src:
        #    img_links.append(src)
    return img_links


def get_wx_nickname(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    try:
        # profile_nickname = soup.find("div", {"class":"profile_inner"})
        pn = soup.find("strong", class_="profile_nickname")  ## 获取公众号名称
    except:
        return ''
    if pn:
        return pn.get_text()
    return ''


# https://mp.weixin.qq.com/s?__biz=MzI0MTc3OTM1NA==&mid=2247484422&idx=2&sn=6229cb99ca977d03789fb20e08d8dc5a&chksm=e90713f3de709ae511b8eb6d41d4c7b5c6540ea3b72510d6ed01e5e58d74e94e26fa0f42c8ab&scene=21#wechat_redirect
# 分享文章没有该字段
def get_wx_account_and_introduction(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    wns = soup.find_all("span", class_="profile_meta_value")
    if wns and len(wns) > 0:
        wx_account = wns[0].get_text()
        intro = wns[-1].get_text()

        return wx_account, intro
    return '', ''
