from bs4 import BeautifulSoup
import re 
html= """
<ul>
    <li><a href="hoge.html">hoge</li>
    <li><a href="https://example.com/fuga">fuga*</li>
    <li><a href="https://example.cm/foo">foo*</li>
    <li><<a href="http://example.com/aaa">aaa</li>
</ul>
"""


bs = BeautifulSoup(html, "html.parser")


datas = bs.findAll(href=re.compile(r"^https://"))

for data in datas:
    print(data.attrs['href'])
