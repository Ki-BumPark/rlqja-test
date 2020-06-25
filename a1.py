from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as parse

url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"

res = req.urlopen(url)
bs = BeautifulSoup(res, "html.parser")

datas = bs.findAll("location")

for data in datas:
    print("지역:", data.city.text, " 날씨:", data.wf.text)

#stnId
