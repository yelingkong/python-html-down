# coding=utf-8
import json

from bs4 import BeautifulSoup
import urllib.request
import ssl

from down.downcss import downcss
from down.downimage import downimg
from down.downjs import downjs
from savepage.savepage import savepage


def main():
    # downurl = "https://youda.com.cn"

    path = 'web'
    # downurl = "http://www.baidu.com/"
    downurl = "https://www.wanjunshijie.com/"
    # downurl = "http://dhz.wanjunshijie.com/"
    jiexi(downurl, path)


def jiexi(downurl, path):

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE"}

    ssl._create_default_https_context = ssl._create_unverified_context
    req = urllib.request.Request(url=downurl, headers=headers)
    res = urllib.request.urlopen(req).read().decode('utf-8')
    res = downjs(res, path, downurl)  # 下载js
    res = downcss(res, path, downurl)  # 下载css
    res = downimg(res, path, downurl)  # 下载css
    savepage(res, 'web/index.html')  # 保存页面


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
