# coding=utf-8
import re
import utils
from bs4 import BeautifulSoup

downpath = "css"


def downcss(res, path, downurl):
    soup = BeautifulSoup(res, 'html.parser')
    for tag in soup.find_all():
        if tag.name in ["link"]:
            if tag.has_attr('href'):
                if bool(re.search('.css', tag['href'])):
                    nameurl = utils.download_file(utils.geturl(tag['href'], downurl), path, downpath + '/')
                    # 下载图片内的文件
                    utils.Handlefile(nameurl, path, downurl)
                    print(nameurl)
                    res = res.replace(tag['href'], nameurl, 1)
    return res
