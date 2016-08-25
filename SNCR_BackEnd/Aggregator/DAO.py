from mysql.connector import (connection)

class DAO:

    def _connect(self):
        self.con = connection.MySQLConnection(user='root', password='',
                                    host='127.0.0.1',
                                    database='NewsData',
                                    charset='utf8')
        return

    def _get_cursor(self):
        """
        Pings connection and returns cursor
        """
        try:
            self.con.ping()
        except:
            self._connect()
        return self.con.cursor()

    def createTable(self):

        cursor = self._get_cursor()
        # Drop table if it already exist using execute() method.
        cursor.execute("DROP TABLE IF EXISTS NewsOrder")

        # Create table as per requirement
        sql = """CREATE TABLE NewsOrder (ID int NOT NULL AUTO_INCREMENT,
                        title  VARCHAR(1000), link  VARCHAR(1000), description VARCHAR(1000), imgLink VARCHAR(1000), category VARCHAR(10), newsId VARCHAR(10), newsSite VARCHAR (80), PRIMARY KEY(ID)) ENGINE = InnoDB DEFAULT CHARSET=utf8"""
        cursor.execute(sql)

    def getHotNews(self):
        cursor = self._get_cursor()
        sql = "select * from NewsOrder"
        cursor.execute(sql)
        newsList = cursor.fetchall()
        cursor.close()

        return newsList

    def insertNews(self,title,link,description,imgLink,category,newsId,newsSite):

        cursor = self._get_cursor()
        sql = """INSERT INTO NewsOrder(title,link,description,imgLink,category,newsId,newsSite) VALUES ('%s','%s','%s','%s','%s','%s','%s') """ %(title, link, description, imgLink, category,newsId,newsSite)

        cursor.execute(sql)
        self.con.commit()


    def selectUncategerizedNews(self):
        cursor = self._get_cursor()
        sql = "select ID from NewsOrder where category='NULL'"
        cursor.execute(sql)
        newsList = cursor.fetchall()
        cursor.close()

        return newsList


    def updateNews(self, ID, category):
        cursor = self._get_cursor()
        sql = "update newsOrder set category = '%s' where ID = '%s'"%(category, ID)
        cursor.execute(sql)
        self.con.commit()
        cursor.close()

    def getDescriptionById(self, ID):
        cursor = self._get_cursor()
        sql = "select description from NewsOrder where ID = '%s'"%(ID)
        cursor.execute(sql)
        description = cursor.fetchall()
        cursor.close()

        return description


