# from html.parser import HTMLParser
# import urllib.request as urllib2
#
# class MyHTMLParser(HTMLParser):
#     def handle_starttag(self, tag, attrs):
#         if tag=="div":
#             print("You are on right way")
#             for attr in attrs:
#                 print("     attr:", attr)
#                 if attr==('class', 'a'):
#                     print("ok")
#
#         print("Encountered a start tag:", tag)
#
#     def handle_endtag(self, tag):
#         print("Encountered an end tag :", tag)
#
#     def handle_data(self, data):
#         print("Encountered some data  :", data)
#
# parser = MyHTMLParser()
# req = urllib2.Request('http://www.hirunews.lk/rss/sinhala.xml')
# res = urllib2.urlopen(req)
#
# print(res.read())
# parser.feed(str(res.read()))
# # parser.feed('<html>'
# #             '<head>'
# #             '<title>Test</title>'
# #             '</head>'
# #             '<div class="a" id="a"><img src="a.png"></div>'
# #             '<div class="b"><img src="b"></div>'
# #             '<body><h1>Parse me!</h1></body>'
# #             '</html>')



import urllib
import urllib.request as urllib2
from bs4 import BeautifulSoup, Comment
from markupsafe import unichr
from mysql.connector import (connection)
import re


db = connection.MySQLConnection(user='root', password='',
                                host='127.0.0.1',
                                database='newsdata',
                                charset='utf8')

# prepare a cursor object using cursor() method
cursor = db.cursor()
cursor.execute("SELECT * FROM NewsOrder")
news = cursor.fetchall()

for row in news:
    title=row[0].replace(" ","")
    asci=ascii(title)
    urlTitle=asci.replace("\\","%")
    url1=row[1]+'/'+urlTitle
    content = urllib2.Request(url1)
    res = urllib2.urlopen(content).read()
    soup = BeautifulSoup(res, "html.parser")
    rows = soup.find_all('div', attrs={"class": "latest-pic"})
    descr=soup.find_all('div', attrs={"class": "lts-txt2"})

    print(descr)
    ans=re.findall('"([^"]*)"', str(rows))

    print(ans[2])


# url='http://www.hirunews.lk/sinhala/133043/%u0dc0%u0dd9%u0dc3%u0d9a%u0dca %u0daf%u0db1%u0dca%u0dc3%u0dd0%u0dbd%u0dca 15%u0da7 %u0db4%u0dd9%u0dbb %u0dbd%u0dd2%u0dba%u0dcf%u0db4%u0daf%u0dd2%u0d82%u0da0%u0dd2 %u0dc0%u0dd2%u0dba %u0dba%u0dd4%u0dad%u0dd4%u0dba%u0dd2'
# # url='http://www.hirunews.lk/sinhala/133069/%E0%B6%A2%E0%B6%82%E0%B6%9C%E0%B6%B8-%E0%B6%AF%E0%B7%94%E0%B6%BB%E0%B6%9A%E0%B6%AE%E0%B6%B1%E0%B6%BA%E0%B7%99%E0%B6%B1%E0%B7%8A-%E0%B6%86-%E0%B6%B8%E0%B7%8F%E0%B6%BB%E0%B6%BA%E0%B7%8F'
# content = urllib2.Request(url)
# res=urllib2.urlopen(content).read()
# soup = BeautifulSoup(res, "html.parser")
# rows =soup.find_all('div',attrs={"class" : "latest-pic"})
# print(rows)
# print(unichr(1234))
# print('aaaaaaaaaaaa')
# for row in soup.find_all('div',attrs={"class" : "latest-pic"}):
#     print(row.text)