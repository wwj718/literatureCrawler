rea#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2016-01-25
# Project: Chinese poem crawler

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

    def poem_page(self, response):
        title = response.doc('DIV.col-md-8>DIV.text-center.b-b.b-2x.b-lt>H3').text()
        author = response.doc('DIV.col-md-8>DIV.row.p-t-sm>DIV.col-xs-12>SPAN').text()
        article = response.doc('HTML>BODY.bg-white>DIV.container>DIV.row>DIV.col-md-8>DIV#content>DIV.m-lg.font14').text()
        return {
              "title":title,
              "author":author,
              "article":article
            }
