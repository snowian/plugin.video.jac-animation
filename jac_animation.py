# -*- coding: UTF-8 -*-
#
# URL template
# srcurl01 = 'http://jac-animation-net.blogspot.tw/'
# patten01_1 = '<a dir=\\\'ltr\\\' href=\\\'.\\\'>(.+?)</a>'
# patten01_2_img = '<a href="(.+?)" imageanchor'
# patten01_2_url = '<div class="jump-link">\\n<a href="(.+?)" title="(.+?)">'
# patten03_url = '<span style="color: orange;">(.+?)<a href="(.+?)">'
#
# DB
# conn.execute("create table anime(id INTEGER PRIMARY KEY AUTOINCREMENT not null, anime_name text not null, anime_srcurl text not null, anime_image)")
# conn.execute("create table anime_video(id INTEGER PRIMARY KEY AUTOINCREMENT not null, animeid int not null, anime_videotitle text not null, anime_videourl text not null)")
#

from bs4 import BeautifulSoup
import urllib.request
import sqlite3 as sqlite

conn = sqlite.connect("jac_urllist.db")

srcurl01 = 'http://jac-animation-net.blogspot.tw/'
urlsrc=urllib.request.urlopen(srcurl01)
pagesrc=BeautifulSoup(urlsrc, 'lxml')
urlsrc.close()

for m in pagesrc.findAll('a', href=True, dir="ltr"):
    urlsrc2=urllib.request.urlopen(m['href'])
    pagesrc2=BeautifulSoup(urlsrc2, 'lxml')
    urlsrc.close()
    hrefdiv2 = pagesrc2.findAll("div", { "class" : "jump-link" })
    for m2 in hrefdiv2.findAll('a', href=True, title=True):
        imgurl = pagesrc2.findAll('a', href=True, imageanchor=True)
        ani_imgurls = imgurl['href']
        ani_name = m2['title']
        ani_srcurl = m2['href']
        cur.execute("insert into anime(anime_name, anime_srcurl, anime_image)values(ani_imgurls,ani_name,ani_srcurl)")
        urlsrc3=urllib.request.urlopen(m2['href'])
        pagesrc3=BeautifulSoup(urlsrc3, 'lxml')
        urlsrc.close()
        hrefdiv3 = pagesrc3.findAll("span", { "style" : "color: orange;" })
        for m3 in hrefdiv3.findAll('a', href=True, title=True):
