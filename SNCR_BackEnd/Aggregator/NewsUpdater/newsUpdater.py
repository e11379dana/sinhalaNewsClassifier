from future_builtins import ascii
import io

import feedparser
import re
import urllib2 as urllib2

from bs4 import BeautifulSoup
# from mysql import (connection)
from mysql.connector import (connection)
from SNCR_BackEnd.Aggregator.DAO import *
from SNCR_BackEnd.Classifier.MNBclassifier import *

class newsUpdater:

    def job(self, link, newsContentClassName, imageClassName, section):
        db = connection.MySQLConnection(user='root', password='',
                                        host='127.0.0.1',
                                        database='NewsData',
                                        charset='utf8')

        # prepare a cursor object using cursor() method
        cursor = db.cursor()

        print("Scheduler is running.......")
        feed = feedparser.parse(link)
        print feed['items']
        for entry in feed['items']:

            length=len(entry['link'].split('/'))

            sql1="SELECT * FROM NewsOrder WHERE newsId >= '%s' and newsSite= '%s'"%(entry['link'].split('/')[length-1],section)
            cursor.execute(sql1)
            result=cursor.fetchall()
            print result
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
                imageRows = soup.find_all('div', attrs={"class": imageClassName})
                imageDetails = re.findall('"([^"]*)"', str(imageRows))

                newsContentRows = soup.find_all('div', attrs={"class": newsContentClassName})

                dao = DAO()
                dao.insertNews(entry['title'], entry['link'], entry['description'].split('<a')[0], imageDetails[2], 'NULL',entry['link'].split('/')[length - 1],section)

            else:
                print 'No new news'

