import feedparser
import urllib.request as urllib2

import re
import schedule
import time

from bs4 import BeautifulSoup
from mysql.connector import (connection)

db = connection.MySQLConnection(user='root', password='',
                                host='127.0.0.1',
                                database='newsdata',
                                charset='utf8')

# prepare a cursor object using cursor() method
cursor = db.cursor()


def job():
    # Drop table if it already exist using execute() method.
    cursor.execute("DROP TABLE IF EXISTS NewsOrder")

    # Create table as per requirement
    sql = """CREATE TABLE NewsOrder (
                title  VARCHAR(1000), link  VARCHAR(1000), description VARCHAR(1000), pubDate VARCHAR(1000), imgLink VARCHAR(11000)) ENGINE = InnoDB DEFAULT CHARSET=utf8"""

    cursor.execute(sql)


    feed = feedparser.parse('http://www.hirunews.lk/rss/sinhala.xml')
    for entry in feed['items']:

        # converting title into a url
        title = entry['title'].replace(" ", "")
        asci = ascii(title)
        urlTitle = asci.replace("\\", "%")
        url = entry['link'] + '/' + urlTitle
        content = urllib2.Request(url)
        res = urllib2.urlopen(content).read()
        soup = BeautifulSoup(res, "html.parser")
        rows = soup.find_all('div', attrs={"class": "latest-pic"})
        ans = re.findall('"([^"]*)"', str(rows))
        print(ans[2])

        sql = "INSERT INTO NewsOrder(title,link,description,imgLink) VALUES ('%s','%s','%s','%s') " % (
        entry['title'], entry['link'], entry['description'],ans[2])

        try:
            cursor.execute(sql)
            db.commit()
        except:
            # Rollback in case there is any error
            db.rollback()

schedule.every(0.1).minutes.do(job)

while 1:
    schedule.run_pending()
    time.sleep(1)