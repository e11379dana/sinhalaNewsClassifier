import feedparser
from flask_restful import Resource

from mysql.connector import (connection)


class main(Resource):
    def get(self):
        db = connection.MySQLConnection(user='root', password='',
                                         host='127.0.0.1',
                                         database='NewsData',
                                         charset='utf8')

        # prepare a cursor object using cursor() method
        cursor = db.cursor()

        cursor.execute("SELECT * FROM NewsOrder")

        news = cursor.fetchall()
        newsList = []

        # print the rows
        for row in news:
            newsList.append({
                'title': row[0],
                'link': row[1],
                'description': row[2]
            })

        db.close()
        return (newsList)

