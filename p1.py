import urllib.request as req

url = "http://uta.pw/shodou/img/28/214.png"
savename = "test.png"

res = req.urlopen(url).read()

with open(savename, mode="wb") as f:
    f.write(res)
    print("saved!")


