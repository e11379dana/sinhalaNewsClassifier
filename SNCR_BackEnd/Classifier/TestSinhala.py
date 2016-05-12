
from Classifier import *
import json
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
with open(spamFile, 'r', encoding=('utf-8-sig')) as f:
    spamKB = json.loads(f.read())
with open(hamFile, 'r', encoding=('utf-8-sig')) as f:
    hamKB = json.loads(f.read())
with open(jamFile, 'r', encoding=('utf-8-sig')) as f:
    jamKB = json.loads(f.read())
with open(pamFile, 'r', encoding=('utf-8-sig')) as f:
    pamKB = json.loads(f.read())
with open(tamFile, 'r', encoding=('utf-8-sig')) as f:
    tamKB = json.loads(f.read())
#print(spamKB)
#print(hamKB)

# obj = json.loads(f, object_hook=_decode_dict)


cl = Classifier(spamKB, hamKB,jamKB,pamKB,tamKB)

f = open('test_sample.txt', 'r',encoding=('utf-8-sig')).read()

print(cl.is_ham(f))
print(cl.is_spam(f))
print(cl.is_jam(f))
print(cl.is_pam(f))
print(cl.is_tam(f))
