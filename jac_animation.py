# -*- coding: UTF-8 -*-
from bs4 import BeautifulSoup
import urllib.request
import gzip, StringIO
import re

srcurl01 = 'http://jac-animation-net.blogspot.tw/'
patten01_1 = '<a dir=\\\'ltr\\\' href=\\\'.\\\'>(.+?)</a>'
patten01_2_img = '<a href="(.+?)" imageanchor'
patten01_2_url = '<div class="jump-link">\\n<a href="(.+?)" title="(.+?)">'
patten03_url = '<span style="color: orange;">(.+?)<a href="(.+?)">'

urlsrc=urllib.request.urlopen(srcurl01)
pagesrc=BeautifulSoup(urlsrc, 'lxml')
urlsrc.close()

for m in pagesrc.findAll('a', href=True, dir="ltr"):
    urlsrc2=urllib.request.urlopen(m['href'])
    pagesrc2=BeautifulSoup(urlsrc2, 'lxml')
    urlsrc.close()
    imgurl = pagesrc2.findAll('a', href=True, imageanchor=True)
    imgurl['href']
    hrefdiv = pagesrc2.findAll("div", { "class" : "jump-link" })
    for m2 in hrefdiv.findAll('a', href=True, title=True):
        m2['title']
        m2['href']
