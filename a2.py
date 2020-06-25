from bs4 import BeautifulSoup
from urllib.request import *
from urllib.parse import *
from os import makedirs
import os.path, time, re


proc_files = {}

def enum_links(html, base):
    bs = BeautifulSoup(html, "html.parser")
    links = bs.select("link[rel='stylesheet']")
    links +=bs.select("a[href]")
    result = []
    for link in links:
        data = link.attrs['href']
        url = urljoin(base, data)
        result.append(url)
    return result

def download_file(url):
    o = urlparse(url)
    savepath = './' + o.netloc + o.path
    if re.search(r"/$", savepath):
        savepath += "index.html"
    savedir = os.path.dirname(savepath)

    if os.path.exists(savepath): return savepath
    if not os.path.exists(savedir):
        print("mkdir:", savedir)
        makedirs(savedir)

    try:
        print("download:", url)
        urlretrieve(url, savepath)
        time.sleep(1)
        return savepath
    except:
        print("다운로드 실패")
        return None

def analyze_html(url, root_url):
    savepath = download_file(url)
    if savepath is None : return
    if savepath in proc_files : return
    proc_files[savepath] = Ture

    html = open(savepath, "r", encoding="utf-8").read()
    links = enum_links(html, url)
    if link in links:
        if link.find(root_url) !=0:
            if not re.search(r".css$", link):continue
        if re.search(r".(html|htm)$", link):
            analyze_html(link, root_url)
            continue
        download_file(link)


if __name__ == "__main__":
    url "https://docs.python.org/3.5/library/"
    analyze_html(url, url)
