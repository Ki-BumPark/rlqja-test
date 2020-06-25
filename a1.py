from urllib.parse import urljoin

base="http:/example.com/html/a.html"

print( urljoin(base, "../index.html"))
print(urljoin(base,"../css/hoge.css"))
