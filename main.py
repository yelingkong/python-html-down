# coding=utf-8
import json

from bs4 import BeautifulSoup
import urllib.request
import ssl
import sys
from down.downcss import downcss
from down.downimage import downimg
from down.downjs import downjs
from savepage.savepage import savepage
import utils


def main():
    if sys.argv[1]:
        downurl = sys.argv[1]

    if not downurl:
        print('请输入下载地址')

    if sys.argv[2]:

        path = sys.argv[2]

    else:
        path = "web"

    if sys.argv[3]:

        file = sys.argv[3]

    else:
        file = "index.html"


    utils.makedir(path)
    jiexi(downurl, path, file)


def jiexi(downurl, path, file):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE",
        "Referer": downurl
    }
    ssl._create_default_https_context = ssl._create_unverified_context
    req = urllib.request.Request(url=downurl, headers=headers)
    res = urllib.request.urlopen(req).read().decode('utf-8')
    res = downjs(res, path, downurl)  # 下载js
    res = downcss(res, path, downurl)  # 下载css
    res = downimg(res, path, downurl)  # 下载img
    savepage(res, path + '/' + file)  # 保存页面
    print('下载完毕')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
