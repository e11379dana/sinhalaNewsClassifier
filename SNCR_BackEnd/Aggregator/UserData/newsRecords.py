from flask_restful import Resource, request
from mysql.connector import (connection)

class userData(Resource):
    def post(self):
        json_obj = request.get_json()
        db = connection.MySQLConnection(user='root', password='1234',
                                        host='127.0.0.1',
                                        database='NewsData',
                                        charset='utf8')

        # prepare a cursor object using cursor() method
        cursor = db.cursor()

        sql = "INSERT INTO UserHistory(UserId,ArticleId) VALUES ('%s','%s') " % (
            json_obj["UserId"],json_obj["ArticleId"])

        try:
            cursor.execute(sql)
            db.commit()
        except Exception as e:
            print e
            # Rollback in case there is any error
            db.rollback()