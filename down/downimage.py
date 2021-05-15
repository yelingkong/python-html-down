# coding=utf-8
import re

import utils
from bs4 import BeautifulSoup

downpath = "images"


# 下载标签
downlist = ['src', 'data-original']
imglist = ['.jpg', '.png', '.jpeg', '.gif', '.svg', '..eot', '.woff', 'ttf']

def downimg(res, path, downurl):
    soup = BeautifulSoup(res, 'html.parser')
    for tag in soup.find_all():
        if tag.name in ["img"]:
            for item in downlist:
                if tag.has_attr(item):
                    for imgitem in imglist:
                        if bool(re.search('data:', item)):
                            print(u"base64图片不需要下载")
                            print(item)
                        elif bool(re.search(imgitem, tag[item])):
                            res = res.replace(tag[item],
                                              utils.download_file(utils.geturl(tag[item], downurl), path + '/',
                                                                  downpath + '/', downurl))

    return res

