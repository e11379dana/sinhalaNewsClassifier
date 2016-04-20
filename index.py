import urllib2
import re
import feedparser

from mysql.connector import (connection)

db = connection.MySQLConnection(user='root', password='1234',
                                 host='127.0.0.1',
                                 database='NewsData',
                                 charset='utf8')

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Drop table if it already exist using execute() method.
cursor.execute("DROP TABLE IF EXISTS NewsOrder")

# Create table as per requirement
sql = """CREATE TABLE NewsOrder (
         News  VARCHAR(1000)) ENGINE = InnoDB DEFAULT CHARSET=utf8"""

cursor.execute(sql)


feed = feedparser.parse('http://www.hirunews.lk/rss/sinhala.xml')
for entry in feed['items']:

    sql = "INSERT INTO NewsOrder(News) VALUES ('%s') " % (entry['title'])
    #print (entry['link'])
    try:
        cursor.execute(sql)
        db.commit()
    except:
        # Rollback in case there is any error
        db.rollback()


cursor.execute("SELECT * FROM NewsOrder")

news = cursor.fetchone()

# print the rows
while news is not None :
    for row in news:
        print row
    news = cursor.fetchone()

db.close()