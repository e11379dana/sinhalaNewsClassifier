from future_builtins import ascii

import feedparser
import re
import schedule
import time
import urllib2 as urllib2

from bs4 import BeautifulSoup
# from mysql import (connection)
from mysql.connector import (connection)

db = connection.MySQLConnection(user='root', password='',
                                host='127.0.0.1',
                                database='newsdata',
                                charset='utf8')

# prepare a cursor object using cursor() method
cursor = db.cursor()
# Drop table if it already exist using execute() method.
cursor.execute("DROP TABLE IF EXISTS newsorder")

# Create table as per requirement
sql = """CREATE TABLE newsorder (ID int NOT NULL AUTO_INCREMENT, title  VARCHAR(1000), link  VARCHAR(1000), description VARCHAR(1000), imgLink VARCHAR(11000), category VARCHAR(100), newsId int, PRIMARY KEY (ID)) ENGINE = InnoDB DEFAULT CHARSET=utf8"""

cursor.execute(sql)

# when first time accessing the news site

feed = feedparser.parse('http://www.hirunews.lk/rss/sinhala.xml')

for entry in feed['items']:

    length = len(entry['link'].split('/'))
    title = entry['title'].replace(" ", "")
    asci = ascii(title)
    asci = asci[1:].replace("'", "")
    urlTitle = asci.replace("\\", "%")
    url = entry['link'] + '/' + urlTitle
    content = urllib2.Request(url)
    res = urllib2.urlopen(content).read()
    soup = BeautifulSoup(res, "html.parser")

    rows = soup.find_all('div', attrs={"class": "latest-pic"})
    ans = re.findall('"([^"]*)"', str(rows))

    sql = "INSERT INTO NewsOrder(title,link,description,imgLink,category,newsId) VALUES ('%s','%s','%s','%s','%s','%s') " % (
        entry['title'], entry['link'], entry['description'], ans[2], 'null', entry['link'].split('/')[length - 1])

    try:
        cursor.execute(sql)
        db.commit()
        print("Scheduler is running.......")
    except Exception as e:
        print e
        # Rollback in case there is any error
        db.rollback()

def job():

    feed = feedparser.parse('http://www.hirunews.lk/rss/sinhala.xml')
    for entry in feed['items']:

        length=len(entry['link'].split('/'))

        sql1="SELECT * FROM newsOrder WHERE newsId >= '%s'"%(entry['link'].split('/')[length-1])
        cursor.execute(sql1)
        result=cursor.fetchall()
        if len(result)==0:
            length = len(entry['link'].split('/'))
            # converting title into a url
            title = entry['title'].replace(" ", "")
            asci = ascii(title)
            asci = asci[1:].replace("'", "")
            urlTitle = asci.replace("\\", "%")
            url = entry['link'] + '/' + urlTitle
            content = urllib2.Request(url)
            res = urllib2.urlopen(content).read()
            try:
                soup = BeautifulSoup(res, "html.parser")
            except:
                print "Error"
            rows = soup.find_all('div', attrs={"class": "latest-pic"})
            ans = re.findall('"([^"]*)"', str(rows))

            sql = "INSERT INTO NewsOrder(title,link,description,imgLink,category,newsId) VALUES ('%s','%s','%s','%s','%s','%s') " % (
                entry['title'], entry['link'], entry['description'], ans[2], 'null', entry['link'].split('/')[length - 1])

            try:
                cursor.execute(sql)
                db.commit()
                print("Scheduler is running.......")
            except:
                # Rollback in case there is any error
                db.rollback()


schedule.every(0.1).minutes.do(job)

while 1:
    schedule.run_pending()
    time.sleep(1)