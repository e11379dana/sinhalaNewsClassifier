import urllib2
import re

from mysql.connector import (connection)

cnx = connection.MySQLConnection(user='root', password='1234',
                                 host='127.0.0.1',
                                 database='NewsData',
                                 charset='utf8')

# prepare a cursor object using cursor() method
cursor = cnx.cursor()

# Drop table if it already exist using execute() method.
cursor.execute("DROP TABLE IF EXISTS NewsOrder")

# Create table as per requirement
sql = """CREATE TABLE NewsOrder (
         News  VARCHAR(1000)) ENGINE = InnoDB DEFAULT CHARSET=utf8"""

cursor.execute(sql)


response = urllib2.urlopen('http://www.hirunews.lk/rss/sinhala.xml')
html = str(response.read())

splitStr = re.split('<title>|</title>',html)

count = 5;
while count < splitStr.__len__():

    # Prepare SQL query to INSERT a record into the database.
    sql = "INSERT INTO NewsOrder(News) VALUES ('%s') " %  (splitStr[count])
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Commit your changes in the database
        cnx.commit()
    except:
        # Rollback in case there is any error
        cnx.rollback()

    count = count + 2

cursor.execute("SELECT * FROM NewsOrder")

news = cursor.fetchone()

# print the rows
for row in news :
    print row

cnx.close()