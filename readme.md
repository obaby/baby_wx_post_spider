微信公众号文章爬虫
===

github上关于微信公众号文章的爬虫还是蛮多的，一搜一大把。基于各种技术，这里分享的是之前的做的基于selenium实现的方法。  

效果：
![screenshot](screenshot/record.gif)
 
 要爬取的公众号列表修改wx_account.py下的内容
 
 微信公众平台账号登录修改baby_wx_post_spider.py下的如下代码：
 ```python
    username = 'root@obaby.org.cn'  # 账号
    password = '********'  # 密码
```

如果要存储数据修改如下代码：
```python
    # add_wx_post(post_title, post_date, content, html_content, pcs, images_link_text, post_url, "2",
    #             wx_account, nickname, wx_intro)
    print('在此处更新数据库')
```
 
> @author: obaby  
> @license: (C) Copyright 2013-2020, obaby@mars.  
> @contact: root@obaby.org.cn  
> @link: http://www.obaby.org.cn  
> @blog: http://www.h4ck.org.cn  
> @findu: http://www.findu.co  