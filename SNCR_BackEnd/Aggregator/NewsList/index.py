import feedparser
from flask_restful import Resource
from SNCR_BackEnd.Aggregator.DAO import *


class main(Resource):
    def get(self, Category):
        dao = DAO()

        if (Category=='hotNews'):
            news = dao.getHotNews()
        else:
            news = dao.getHotNews()

        newsList = []

        print news
        # print the rows
        for row in news:
            spltDescription = unicode(row[3]).split("<a")
            newsList.append({
                'title': row[1],
                'link': row[2],
                'description': spltDescription[0],
                'image': row[4],
                'articleId': row[6]

            })

        return (newsList)

