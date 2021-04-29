import requests
import re
from urllib.parse import urlparse
import os


# 下载文件
def download_file(url, save_path=""):
    print('下载文件:' + url)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE"}
    r = requests.get(url, headers=headers)
    with open(save_path + getFileName(url), "wb") as code:
        code.write(r.content)


def getFileName(s):
    str = re.findall(r'[^/]+(?!.*/)', s)[0]
    head, sep, tail = str.partition('?')
    return (head)


# 域名处理
def geturl(s, downurl):
    if (urlparse(s).netloc):
        if (urlparse(s).scheme):
            return urlparse(s).scheme + '://' + urlparse(s).netloc + urlparse(s).path
        else:
            return 'http://' + urlparse(s).netloc + urlparse(s).path
    else:
        return urlparse(downurl).scheme + '://' + urlparse(downurl).netloc + '/' + s


def makedir(path):
    if not os.path.exists(path):
        os.mkdir(path)
