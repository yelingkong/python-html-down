# coding=utf-8
import re

import utils
from bs4 import BeautifulSoup

downpath = "images"


def downimg(res, path, downurl):
    soup = BeautifulSoup(res, 'html.parser')
    for tag in soup.find_all():
        if tag.name in ["img"]:
            if tag.has_attr('src'):
                # 如果图片不是base64
                if not bool(re.search('data:', tag['src'])):
                    res = res.replace(tag['src'],
                                      utils.download_file(utils.geturl(tag['src'], downurl), path + '/',
                                                          downpath + '/', downurl))
            ##懒加载图片
            if tag.has_attr('data-original'):
                res = res.replace(tag['data-original'],
                                  utils.download_file(utils.geturl(tag['data-original'], downurl), path + '/',
                                                      downpath + '/', downurl))
            # res = res.replace(tag['src'], downpath + '/' + utils.getFileName(tag['src']))
            # utils.download_file(utils.geturl(tag['src'], downurl), path + '/' + downpath + '/')

            #     print('base64图片不需要下载')
            # elif bool(re.search('../', item)):
            #     download_file(geturl(replacex(item), downurl), path, 'images/', downurl)
            # else:
            #     item = replacex(item)
            #     download_file(geturl(replacex(item), downurl), path, 'images/', downurl)
    return res
