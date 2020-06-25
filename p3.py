import urllib.request as req
import urllib.parse as parse
import sys

if len(sys.argv) <=1:
    print("input param")
    sys.exit()

regionNumber = sys.argv[1]

url ="http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"

value = {

    "stnId" : regionNumber

}

params = parse.urlencode(value)

api = url + '?' + params


res = req.urlopen(api).read()

result = res.decode("utf-8")
print(result)
