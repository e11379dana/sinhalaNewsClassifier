
from Classifier import *
import json
import io
from mysql.connector import (connection)
def _decode_list(data):
    rv = []
    for item in data:
        if isinstance(item, unicode):
            item = item.encode('utf-8')
        elif isinstance(item, list):
            item = _decode_list(item)
        elif isinstance(item, dict):
            item = _decode_dict(item)
        rv.append(item)
    return rv

def _decode_dict(data):
    rv = {}
    for key, value in data.iteritems():
        if isinstance(key, unicode):
            key = key.encode('utf-8')
        if isinstance(value, unicode):
            value = value.encode('utf-8')
        elif isinstance(value, list):
            value = _decode_list(value)
        elif isinstance(value, dict):
            value = _decode_dict(value)
        rv[key] = value
    return rv


spamFile = 'arts_culture_entertainment.json'
hamFile = 'defence.json'
jamFile = 'economy_business_finance.json'
pamFile = 'political.json'
tamFile = 'sport.json'

# f = open(newFile, 'wb').write(b'\xef\xbb\xbf{"data":\r\n    {"mobileHelp":\r\n        {"value":\r\n            {\r\n            "ID1":{"children": [1,2,3,4,5]},\r\n            "ID2":{"children": []},\r\n            "ID3":{"children": [6,7,8,9,10]}\r\n            }\r\n        }\r\n    }\r\n}')

# print(byteify(newFile))
with io.open(spamFile, 'r', encoding=('utf-8-sig')) as f:
    spamKB = json.loads(f.read())
with io.open(hamFile, 'r', encoding=('utf-8-sig')) as f:
    hamKB = json.loads(f.read())
with io.open(jamFile, 'r', encoding=('utf-8-sig')) as f:
    jamKB = json.loads(f.read())
with io.open(pamFile, 'r', encoding=('utf-8-sig')) as f:
    pamKB = json.loads(f.read())
with io.open(tamFile, 'r', encoding=('utf-8-sig')) as f:
    tamKB = json.loads(f.read())
#print(spamKB)
#print(hamKB)

# obj = json.loads(f, object_hook=_decode_dict)


cl = Classifier(spamKB, hamKB,jamKB,pamKB,tamKB)

db = connection.MySQLConnection(user='root', password='ilovepera',
                                host='127.0.0.1',
                                database='NewsData',
                                charset='utf8')

# prepare a cursor object using cursor() method
cursor = db.cursor()

cursor.execute("SELECT * FROM NewsOrder")

news = cursor.fetchall()
for row in news:
    if row[5]=="null":
        file=io.open('test_sample.txt', 'w', encoding=('utf-8-sig'))
        file.write(row[3])
        f = io.open('test_sample.txt', 'r', encoding=('utf-8-sig')).read()
        defence=cl.is_ham(f)
        sport=cl.is_tam(f)
        art=cl.is_spam(f)
        politics=cl.is_pam(f)
        economy=cl.is_jam(f)
        if art['result']:
            sql = "UPDATE NewsOrder SET category = 'art' WHERE ID = '%s'" % (row[0])
        elif defence['result']:
            sql = "UPDATE NewsOrder SET category = 'defence' WHERE ID = '%s'" % (row[0])
        elif economy['result']:
            sql = "UPDATE NewsOrder SET category = 'economy' WHERE ID = '%s'" % (row[0])
        elif politics['result']:
            sql = "UPDATE NewsOrder SET category = 'politics' WHERE ID = '%s'" % (row[0])
        else:
            sql = "UPDATE NewsOrder SET category = 'sport' WHERE ID = '%s'" % (row[0])

        cursor.execute(sql)
        db.commit()
        print(cl.is_ham(f))
        print(cl.is_spam(f))
        print(cl.is_jam(f))
        print(cl.is_pam(f))
        print(cl.is_tam(f))
