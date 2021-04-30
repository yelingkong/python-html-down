# coding=utf-8
import re
import utils
from bs4 import BeautifulSoup

downpath = "css"


def downcss(res, path, downurl):
    soup = BeautifulSoup(res, 'html.parser')
    utils.makedir(path + '/' + downpath)
    for tag in soup.find_all():
        if tag.name in ["link"]:
            if tag.has_attr('href'):
                if bool(re.search('.css', tag['href'])):
                    print(tag['href'])
                    res = res.replace(tag['href'],
                                      utils.download_file(utils.geturl(tag['href'], downurl), path, downpath + '/'))
                    # res = res.replace(tag['href'], 'css/' + utils.getFileName(tag['href']))
                    # utils.download_file(utils.geturl(tag['href'], downurl), path + '/css/')
    return res
