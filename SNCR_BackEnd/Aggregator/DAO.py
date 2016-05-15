from mysql.connector import (connection)

class DAO:

    def _connect(self):
        con = connection.MySQLConnection(user='root', password='1234',
                                    host='127.0.0.1',
                                    database='NewsData',
                                    charset='utf8')
        # prepare a cursor object using cursor() method
        self.cursor = con.cursor()

        return


    def createTable(self):
        # Drop table if it already exist using execute() method.
        self.cursor.execute("DROP TABLE IF EXISTS NewsOrder")

        # Create table as per requirement
        sql = """CREATE TABLE NewsOrder (
                        title  VARCHAR(1000), link  VARCHAR(1000), description VARCHAR(1000), pubDate VARCHAR(1000), category VARCHAR(10)) ENGINE = InnoDB DEFAULT CHARSET=utf8"""

        self.cursor.execute(sql)

    def getDescription(self):
        sql = "select dscription from "