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

日志效果：  
```batch
H:\PyCharmProjects\baby_wx_spider\venv\Scripts\python.exe H:/PyCharmProjects/baby_wx_spider/baby_wx_post_spider.py
****************************************************************************************************
Wechat Post Spider System
By：obaby
http://www.h4ck.org.cn
http://www.obaby.org.cn
http://www.findu.co
****************************************************************************************************
[*] System starting ..................
[*] Try to login with username:obaby.lh@163.com Password: ***************
[*] Please scan the qrcode to continue
[*] Scan the QRCode with your cell phone to login!!
[*] Spider starting.....................
[*] Current Wechat account is:
青岛文旅
[*] all passed!
[*] Link:http://mp.weixin.qq.com/s?__biz=MzU0NTc4OTI5MQ==&mid=2247490126&idx=1&sn=29a88b4ceef1cdbd6584702fdd46112a&chksm=fb66de4acc11575c946e802cb475845d7ff540d5a0d6da23834c0c4caa27bd3c3b7c2dd762e6#rd
在此处更新数据库
[*] Link:http://mp.weixin.qq.com/s?__biz=MzU0NTc4OTI5MQ==&mid=2247490126&idx=2&sn=87724f394f1533a23f50e5fddf7c88c1&chksm=fb66de4acc11575cb5c3a610371936a14f2743916b332f0bea3a3edc63dc2648351b386a0b95#rd
在此处更新数据库
[*] Link:http://mp.weixin.qq.com/s?__biz=MzU0NTc4OTI5MQ==&mid=2247490126&idx=3&sn=a9a3992058f069149102ea0fd9dae0b4&chksm=fb66de4acc11575c2c0ef3afe8c5de6c2e8b432c1b3d6c3e8d69f5cb439a85962517b147ee8b#rd
在此处更新数据库
```

 PS: 代码如果发现bug，请自行修改！由于微信后台一直变化，所以如果代码不能运行，重新定位相关的元素更新xpath即可  
 
> @author: obaby  
> @license: (C) Copyright 2013-2020, obaby@mars.  
> @contact: root@obaby.org.cn  
> @link: http://www.obaby.org.cn  
> @blog: http://www.h4ck.org.cn  
> @findu: http://www.findu.co  