
#!/usr/bin/env python
# -*- encoding: utf-8 -*-

#注意：火柴盒是每天发布的：http://www.huochaihe.com/jingxuan.php
#写为定时爬虫

##任务：抓取内容，按点赞数排序

#似乎采用mongo数据库查询比较容易


'''
页面结构分析
元素：
发布时间
<div class="line_bread mt50 mb10">
        <h3 class="fstyle">发布时间：2016年01月13日</h3>
</div>    
每天内容：
div class="in_img_list clearfix" : 每天三篇内容
  ul li
    一首歌 eq(0)
    一首诗 eq(1)
    一篇文章 eq(2)
    
'''

'''
#jquery实验
#用jquery实验一下：
$("DIV.in_img_list.clearfix>UL>LI").length //45
$("div.line_bread h3.fstyle").length //15
$(".in_img_list.clearfix").length //15
'''

from pyspider.libs.base_handler import *
import re

class Handler(BaseHandler):
    crawl_config = {
    }

    def on_start(self, response):
        self.crawl('http://www.huochaihe.com/jingxuan.php', callback=self.day_section)

        
      

    def day_section(self, response):
        '''
        response.doc是一个pyquery对象，有类似jquery的方法，参考：
                https://pythonhosted.org/pyquery/api.html
        '''
        date_list =  response.doc("div.line_bread h3.fstyle").items()
        date_content_list = response.doc(".in_img_list.clearfix").items()
        for (date,date_content) in zip(date_list,date_content_list):
            music_box = date_content.eq(0) #音乐
            poem_box = date_content.eq(1) #诗歌
            article_box = date_content.eq(2) #文章
            date_text = date.text()
            #print date.text() #todo：转化为标准时间
            date_data = (music_box,poem_box,article_box,date_text)
            self.save_data(date_data)
            #以天为存储单位吧
            #box_type
            #eq0 = date_content.eq(0).text()
            #print eq0
            break
            
    def save_data(self,date_data):
        #分门别类来存储
        (music_box,poem_box,article_box,date_text)= date_data
        self.save_music_box(music_box,date_text)
                    
    
    def save_music_box(self,music_box,date_text):
        type = "music_box"
        pic_url = music_box.find(".in_img_box img").attr("src")
        music_url = music_box.find("source").attr("src")
        music_name = music_box.find(".in_bigtxt.f18.fblue").text()
        up_count = music_box.find(".in_num_box01").text()
        sharing_count =  music_box.find(".in_num_box02").text()
        #print pic_url,date_text,type
        result = {
            "date" : date_text,
            "data_type" : type,
            "up_count":up_count,
            "sharing_count":sharing_count,
            "data" :  {"pic_url":pic_url,
                       "music_url":music_url,
                       "music_name":music_name
                       }
            }   
        print result
        return result 

    def save_poem_box(self,poem_box,date_text):
        type = "poem_box"
        pic_url = music_box.find(".in_img_box img").attr("src")
        music_url = music_box.find("source").attr("src")
        music_name = music_box.find(".in_bigtxt.f18.fblue").text()
        #print pic_url,date_text,type
        result = {
            "date" : date_text,
            "data_type" : type,
            "data" :  {"pic_url":pic_url,
                       "music_url":music_url,
                       "music_name":music_name
                       }
            }   
        print result
        return result 

    def save_article_box(self,article_box,date_text):
        type = "article_box"
        pic_url = music_box.find(".in_img_box img").attr("src")
        music_url = music_box.find("source").attr("src")
        music_name = music_box.find(".in_bigtxt.f18.fblue").text()
        #print pic_url,date_text,type
        result = {
            "date" : date_text,
            "data_type" : type,
            "data" :  {"pic_url":pic_url,
                       "music_url":music_url,
                       "music_name":music_name
                       }
            }   
        print result
        return result 
