import urllib.request as req

url = "http://api.aoikujira.com/ip/ini"

res = req.urlopen(url)
data = res.read()

data = data.decode("utf-8")
print(data)
