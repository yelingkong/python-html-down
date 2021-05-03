# coding=utf-8
import utils
from bs4 import BeautifulSoup

downpath = "images"


def downimg(res, path, downurl):
    soup = BeautifulSoup(res, 'html.parser')
    for tag in soup.find_all():
        if tag.name in ["img"]:
            if tag.has_attr('src'):
                res = res.replace(tag['src'],
                                  utils.download_file(utils.geturl(tag['src'], downurl), path + '/',
                                                      downpath + '/'))
                # res = res.replace(tag['src'], downpath + '/' + utils.getFileName(tag['src']))
                # utils.download_file(utils.geturl(tag['src'], downurl), path + '/' + downpath + '/')
    return res
