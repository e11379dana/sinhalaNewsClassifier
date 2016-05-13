import feedparser
import schedule
import time
from mysql.connector import (connection)

db = connection.MySQLConnection(user='root', password='1234',
                                host='127.0.0.1',
                                database='NewsData',
                                charset='utf8')

# prepare a cursor object using cursor() method
cursor = db.cursor()


def job():
    # Drop table if it already exist using execute() method.
    cursor.execute("DROP TABLE IF EXISTS NewsOrder")

    # Create table as per requirement
    sql = """CREATE TABLE NewsOrder (
                title  VARCHAR(1000), link  VARCHAR(1000), description VARCHAR(1000), pubDate VARCHAR(1000), category VARCHAR(10)) ENGINE = InnoDB DEFAULT CHARSET=utf8"""

    cursor.execute(sql)


    feed = feedparser.parse('http://www.hirunews.lk/rss/sinhala.xml')
    for entry in feed['items']:
        description = entry['description'].split("..")
        print description
        sql = "INSERT INTO NewsOrder(title,link,description) VALUES ('%s','%s','%s') " % (entry['title'],entry['link'],description[0])
        #print (entry['link'])
        try:
            cursor.execute(sql)
            db.commit()
            print "Schedular is running"
        except:
            # Rollback in case there is any error
            db.rollback()


schedule.every(10).minutes.do(job)

while 1:
    schedule.run_pending()
    time.sleep(1)