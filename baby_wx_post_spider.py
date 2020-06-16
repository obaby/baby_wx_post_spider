# coding: utf-8

import pickle
import random
import time

from colorama import init, Fore, Style
from selenium import webdriver

from wx_account import wx_account
from wx_analyze import *


def qsprint(dict_or_list):
    print(u'[*] DATA:' + json.dumps(dict_or_list, encoding="UTF-8", ensure_ascii=False))


def login(username, password):
    # 打开微信公众号登录页面
    driver.get('https://mp.weixin.qq.com/')
    driver.maximize_window()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="header"]/div[2]/div/div/div[2]/a').click()
    # # 自动填充帐号密码
    driver.find_element_by_xpath('//*[@id="header"]/div[2]/div/div/div[1]/form/div[1]/div[1]/div/span/input').clear()
    driver.find_element_by_xpath('//*[@id="header"]/div[2]/div/div/div[1]/form/div[1]/div[1]/div/span/input').send_keys(
        username)
    driver.find_element_by_xpath('//*[@id="header"]/div[2]/div/div/div[1]/form/div[1]/div[2]/div/span/input').clear()
    driver.find_element_by_xpath('//*[@id="header"]/div[2]/div/div/div[1]/form/div[1]/div[2]/div/span/input').send_keys(
        password)
    #
    time.sleep(1)
    #
    # # 自动点击登录按钮进行登录
    driver.find_element_by_xpath('//*[@id="header"]/div[2]/div/div/div[1]/form/div[4]/a').click()
    if driver.find_element_by_class_name('verifycode'):
        print('[*] Please scan the qrcode to continue')
        time.sleep(10)
    # 拿手机扫二维码！
    time.sleep(10)


def open_link(nickname):
    # 进入新建图文素材
    # driver.find_element_by_xpath('//*[@id="menuBar"]/li[4]/ul/li[3]/a/span/span').click()
    # //*[@id="js_main"]/div[3]/div[1]/div[2]/div[2]/div/a[1]
    driver.find_element_by_xpath('//*[@id="js_main"]/div[3]/div[1]/div[2]/button').click()
    time.sleep(10)

    # 切换到新窗口
    for handle in driver.window_handles:
        if handle != driver.current_window_handle:
            driver.switch_to_window(handle)

    # 点击超链接
    driver.find_element_by_xpath('//*[@id="js_editor_insertlink"]').click()
    time.sleep(3)
    # # 点击查找文章
    driver.find_element_by_xpath('//*[@id="vue_app"]/div[5]/div[1]/div/div[2]/div[2]/form[1]/div[3]/div/div/p/button').click()
    # 输入公众号名称
    driver.find_element_by_xpath('//*[@id="vue_app"]/div[5]/div[1]/div/div[2]/div[2]/form[1]/div[3]/div/div/div/div/span/input').clear()
    driver.find_element_by_xpath('//*[@id="vue_app"]/div[5]/div[1]/div/div[2]/div[2]/form[1]/div[3]/div/div/div/div/span/input').send_keys(nickname)
    # 点击搜索
    driver.find_element_by_xpath('//*[@id="vue_app"]/div[5]/div[1]/div/div[2]/div[2]/form[1]/div[3]/div/div/div/div/span/span/button[2]').click()
    time.sleep(3)
    # 点击第一个公众号
    try:
        # 公众号搜索过于频繁 操作太频繁，请稍后再试
        '''
        <p class="js_acc_search_tips frm_msg fail" style="display: block;">
                        <span class="frm_msg_content">操作太频繁，请稍后再试</span>
                    </p>
        '''
        # driver.find_element_by_xpath('//*[@id="myform"]/div[3]/div[3]/div[2]/div/div[1]/div/div[1]/div[3]/p[2]').click()
        driver.find_element_by_xpath('//*[@id="vue_app"]/div[5]/div[1]/div/div[2]/div[2]/form[1]/div[3]/div/div/div/div[2]/ul/li').click()
    except:
        global is_need_change_account
        is_need_change_account = True
    time.sleep(3)


'''
<div class="search_article_result">
                        <div class="info_box">
                            <div class="inner">
                                <div class="info_hd">
                                    <div class="ext_info"></div>
                                    <h4>
                                        <span class="frm_input_box search with_del append ">
                                            <a style="display:none;" class="js_article_search_del del_btn" href="javascript:">
                                                <i class="icon_search_del"></i>&nbsp;
                                            </a>
                                            <a href="javascript:" class="js_article_search_btn frm_input_append">
                                                <i class="icon16_common search_gray">搜索</i>&nbsp;
                                            </a>
                                            <input type="text" value="" class="js_article_search_input frm_input" placeholder="输入文章名查找公众号群发过的文章">
                                        </span>
                                    </h4>
                                </div>
                                <div class="info_bd tc">
                                    <i style="display: none;" class="js_article_loading icon_loading_small white"></i>
                                    <div class="js_article_list" style="display: block;">
<div class="media_list_tips_wrp tips_global">
	<span class="tips">操作太频繁，请稍后再试</span>
	<span class="vm_box"></span>
</div>
</div>
                                </div>
                            </div>
                            <!--BEGIN 分页-->
                            <div class="js_article_pagebar pagination_wrp" style="display: none;"></div>
                            <!--END 分页-->
                        </div>
                    </div>
'''


def get_url_title(html):
    try:
        tips = driver.find_element_by_xpath("//*[contains(text(),'操作太频繁')]")
        if tips:
            print('[*] Account current banded!!!!!!!')
            global is_need_change_account
            is_need_change_account = True
            return []
    except:
        print('[*] all passed!')
    lst = []
    for item in driver.find_elements_by_class_name('inner_link_article_item'):
        post_date = item.text.split('\n')[0]
        post_url = item.find_element_by_tag_name('a').get_attribute('href')
        post_title = item.text.split('\n')[1]
        temp_dict = {
            'date': post_date,
            'url': post_url,
            'title': post_title,
        }
        print('[*] Link:' + post_url)
        global current_isfirstpost, current_nickname
        #  更新爬虫相关数据
        if current_isfirstpost:
            # spider_update_wx_account_first_post_date(current_nickname, post_date)
            current_isfirstpost = False
        else:
            # spider_update_wx_account_last_post_date(current_nickname, post_date)
            pass
        #  检测是否已经爬取过信息，如果爬取过，直接跳过，处理下一个
        # if not check_is_post_crawled(post_title, current_nickname, post_date,post_url):
        if True:
            #  获取文章相关的信息
            html_content = get_wxpost_html_content(post_url)
            if not html_content or html_content == '':
                with open('error.log', 'wb') as f:
                    f.write(post_url)
            else:
                title, content = get_wxpost_text_title_content(html_content)
                ps = get_wxpost_all_p(html_content)
                pcs = '\n'.join(ps)
                imgs = get_wxpost_img_links(html_content)
                images_link_text = '\n'.join(imgs)
                nickname = get_wx_nickname(html_content)
                wx_account, wx_intro = get_wx_account_and_introduction(html_content)
                #  提交数据到服务器
                if wx_account == '' and wx_intro == '':
                    print('[*] forward post have no data!!')
                else:
                    # add_wx_post(post_title, post_date, content, html_content, pcs, images_link_text, post_url, "2",
                    #             wx_account, nickname, wx_intro)
                    print('在此处更新数据库')
                    ts = random.randint(2, 5)
                    time.sleep(ts)
                # lst.append(temp_dict)
                # qsprint(temp_dict)
        else:
            print('already crawled')
            global is_in_force_mode  # 非暴力模式下主动结束
            if not is_in_force_mode:
                global is_finish_current_account
                is_finish_current_account = True
                break

    return lst


def get_wx_posts(nickname):
    open_link(nickname)
    try:
        page_num = int(driver.find_elements_by_class_name('weui-desktop-pagination__num')[-1].text.split('/')[-1].lstrip())
    except Exception as e:
        print(e)
        page_num = 1  # 搜索结果只有一页

    # 记录 executor_url 和 session_id 以便复用session
    executor_url = driver.command_executor._url
    session_id = driver.session_id

    global is_in_force_mode

    if not is_in_force_mode:
        page_num = 2
    print(page_num)
    # 点击下一页
    url_title_lst = get_url_title(driver.page_source)

    for _ in range(1, page_num):  # for _ in range(1, page_num)
        global is_finish_current_account
        if is_finish_current_account:
            break
        try:
            pagination = driver.find_elements_by_class_name('pagination')[1]
            print(pagination)
            but = pagination.find_elements_by_tag_name('a')[2]
            print(but)
            but.click()
            time.sleep(5)
            url_title_lst += get_url_title(driver.page_source)
            # driver.find_element_by_xpath('//*[@id="wxPagebar_1546065827119"]/span[1]/a[3]/i').click()
            # time.sleep(5)
            # url_title_lst += get_url_title(driver.page_source)
        except:
            # 保存
            with open('data.pickle', 'wb') as f:
                pickle.dump(url_title_lst, f)
            print("[*] 第{}页失败".format(_))
            break


def random_scroll():
    for x in range(2):
        js = "var q=document.documentElement.scrollTop=" + str(x * 500)
        driver.execute_script(js)
        time.sleep(10)
    for x in range(2):
        js = "var q=document.documentElement.scrollTop=-" + str(x * 500)
        driver.execute_script(js)
        time.sleep(10)


def print_hello():
    print("*" * 100)
    print("Wechat Post Spider System")
    print("By：obaby")
    print("http://www.h4ck.org.cn")
    print("http://www.obaby.org.cn")
    print("http://www.findu.co")
    print("*" * 100)


if __name__ == "__main__":
    # 初始化颜色
    # 微信账号禁止搜索时间大约1小时
    init()
    global current_isfirstpost
    global current_nickname
    global is_need_change_account
    global is_finish_current_account
    global is_in_force_mode
    is_finish_current_account = False
    current_nickname = u''
    current_isfirstpost = True  # 是否第一次爬取
    is_need_change_account = False
    is_in_force_mode = False
    # 用webdriver启动谷歌浏览器
    # https://sites.google.com/a/chromium.org/chromedriver/home
    # driver = webdriver.Chrome(executable_path='/home/lu/Downloads/chromedriver2.36')
    print_hello()
    print('[*] System starting ..................')
    driver = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')

    username = 'root@obaby.org.cn'  # 账号
    password = '********'  # 密码
    print('[*] Try to login with username:' + Fore.RED + username + Style.RESET_ALL + ' Password: ***************')
    login(username, password)
    print('[*] Scan the QRCode with your cell phone to login!!')
    print('[*] Spider starting.....................')

    driver.find_element_by_xpath('//*[@id="menuBar"]/li[5]/ul/li[3]/a/span/span').click()

    for nickname in wx_account:
        # nickname = wx_nick_name
        print(u'[*] Current Wechat account is:')
        print(Fore.CYAN)
        print(nickname)
        print(Style.RESET_ALL)
        current_nickname = nickname
        current_isfirstpost = True
        get_wx_posts(nickname)
        # driver.close()
        time.sleep(5)
        # New tabs will be the last object in window_handles
        driver.switch_to.window(driver.window_handles[-1])
        # close the tab
        driver.close()
        # switch to the main window
        driver.switch_to.window(driver.window_handles[0])
        print('[*] Update wechat account crawled date.')
        # spider_update_wx_account_crawled_date(current_nickname)
        if is_need_change_account:
            print('[*] Change your account to continue!!!')
            break
            for x in range(60):
                print('[*] Random scroll..')
                print('[*] Current is: ' + str(x) + ' total: 60')
                random_scroll()
        print('[*] Tab close, start to crawling another account.')
    driver.quit()
