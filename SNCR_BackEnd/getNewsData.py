from html.parser import HTMLParser
import urllib.request as urllib2

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag=="div":
            print("You are on right way")
            for attr in attrs:
                print("     attr:", attr)
                if attr==('class', 'a'):
                    print("ok")

        print("Encountered a start tag:", tag)

    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)

    def handle_data(self, data):
        print("Encountered some data  :", data)

parser = MyHTMLParser()
req = urllib2.Request('http://www.hirunews.lk/sinhala/business/133066')
res = urllib2.urlopen(req)

print(res.read())
parser.feed(res.read().decode("utf-8"))
# parser.feed('<html>'
#             '<head>'
#             '<title>Test</title>'
#             '</head>'
#             '<div class="a" id="a"><img src="a.png"></div>'
#             '<div class="b"><img src="b"></div>'
#             '<body><h1>Parse me!</h1></body>'
#             '</html>')