# -*- ereated on 2016-01-25
# Project: Chinese poem crawler
#HTML>BODY.bg-white>DIV.container.z-container>DIV.row>DIV.col-md-8>DIV.m-md>DIV.font14>DIV.m-t-lg.m-g-lg.text-center>DIV>UL.pagination>LI>A
#HTML>BODY.bg-white>DIV.container.z-container>DIV.row>DIV.col-md-8>DIV.m-md>DIV.font14>DIV.m-t-lg.m-g-lg.text-center>DIV>UL.pagination>LI>A

from pyspider.libs.base_handler import *
import re

class Handler(BaseHandler):
    crawl_config = {
    }
    global baseurl

    def on_start(self):
        baseurl  = 'http://www.zgshige.com/myjx/'
        self.crawl(baseurl, callback=self.index_page)

    def index_page(self, response):
        for each in response.doc('UL.list-unstyled.lh20>LI>a').items():
            print each.attr.href
            self.crawl(each.attr.href , callback=self.poem_page)
        for each in response.doc('UL.pagination>LI>a').items():
            print 'check pagination url ===>> ' + each.attr.href
            self.crawl(each.attr.href , callback=self.poem_page_list)
    
    def poem_page_list(self, response):
          for each in response.doc('UL.list-unstyled.lh20>LI>a').items():
            print each.attr.href
            self.crawl(each.attr.href , callback=self.poem_page)
          for each in response.doc('UL.pagination>LI>a').items():
            print 'check pagination url ===>> ' + each.attr.href
            self.crawl(each.attr.href , callback=self.poem_page_list)

    def poem_page(self, response):
        title = response.doc('DIV.col-md-8>DIV.text-center.b-b.b-2x.b-lt>H3').text()
        author = response.doc('DIV.col-md-8>DIV.row.p-t-sm>DIV.col-xs-12>SPAN').text()
        article = response.doc('HTML>BODY.bg-white>DIV.container>DIV.row>DIV.col-md-8>DIV#content>DIV.m-lg.font14').text()
        return {
              "title":title,
              "author":author,
              "article":article,
              "tag":"poem"
            }
