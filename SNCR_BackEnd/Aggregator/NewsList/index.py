import feedparser
from flask_restful import Resource

from mysql.connector import (connection)


class main(Resource):
    def get(self, Category):
        db = connection.MySQLConnection(user='root', password='1234',
                                         host='127.0.0.1',
                                         database='NewsData',
                                         charset='utf8')

        # prepare a cursor object using cursor() method
        cursor = db.cursor()

        print Category

        if (Category=='hotNews'):
            sql = "SELECT * FROM NewsOrder"
        else:
            sql = "SELECT * FROM NewsOrder WHERE category = '%s'"%(Category);


        cursor.execute(sql)
        news = cursor.fetchall()
        newsList = []

        print news
        # print the rows
        for row in news:
            newsList.append({
                'title': row[0],
                'link': row[1],
                'description': row[2]
            })

        db.close()
        return (newsList)

