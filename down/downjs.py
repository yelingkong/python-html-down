# coding=utf-8
import re
import utils
from bs4 import BeautifulSoup

downpath = "js"

def downjs(res, path, downurl):
    soup = BeautifulSoup(res, 'html.parser')
    utils.makedir(path + '/' + downpath)
    for tag in soup.find_all():
        if tag.name in ["script"]:
            if tag.has_attr('src'):
                print(tag['src'])
                if bool(re.search('.js', tag['src'])):
                    res = res.replace(tag['src'], '/js/' + utils.getFileName(tag['src']))
                    utils.download_file(utils.geturl(tag['src'], downurl), path + '/js/')
    return res