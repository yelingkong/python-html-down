# coding=utf-8
import re

import utils
from bs4 import BeautifulSoup

downpath = "images"

# 下载标签
downlist = ['src', 'data-original']


def downimg(res, path, downurl):
    soup = BeautifulSoup(res, 'html.parser')
    for tag in soup.find_all():
        if tag.name in ["img"]:
            for item in downlist:
                if tag.has_attr(item):
                    # 如果图片不是base64
                    if not bool(re.search('data:', tag[item])):
                        res = res.replace(tag[item],
                                          utils.download_file(utils.geturl(tag[item], downurl), path + '/',
                                                              downpath + '/', downurl))

    return res

