# coding=utf-8

import urllib.request
import ssl
from down.downcss import downcss
from down.downimage import downimg
from down.downjs import downjs
from savepage.savepage import savepage
import utils
import sys


def main():
    downurl = "https://www.baidu.com"  # 需要下载的地址
    path = 'web'  # 要保存的目录
    file = 'index.html'  # 要保存的文件名
    # downurl = sys.argv[1]  # 需要下载的地址 如https://www.wanjunshijie.com
    # path = sys.argv[2]  # 要保存的目录 如 web
    # file = sys.argv[3]  # 要保存的文件名 如 index.html
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
    print(u"开始下载...")
    res = downjs(res, path, downurl)  # 下载js
    res = downcss(res, path, downurl)  # 下载css
    res = downimg(res, path, downurl)  # 下载img
    # 下载页面css内的图片
    res = utils.downCssbg(res, path, downurl)
    savepage(res, path + '/' + file)  # 保存页面

    print(u"下载完毕.")


if __name__ == '__main__':
    main()
