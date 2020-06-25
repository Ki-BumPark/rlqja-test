from bs4 import BeautifulSoup
import urllib.request as req

url = "https://finance.naver.com/marketindex/"

res = req.urlopen(url)
bs = BeautifulSoup(res, "html.parser")

usd_data = bs.select_one("#exchangeList > li.on > a.head.usd > div > span.value")

print("USD: ", usd_data.text)
