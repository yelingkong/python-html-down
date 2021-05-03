# coding=utf-8
import re
import utils
from bs4 import BeautifulSoup

downpath = "js"


def downjs(res, path, downurl):
    soup = BeautifulSoup(res, 'html.parser')
    for tag in soup.find_all():
        if tag.name in ["script"]:
            if tag.has_attr('src'):
                print(tag['src'])
                if bool(re.search('.js', tag['src'])):
                    res = res.replace(tag['src'],
                                      utils.download_file(utils.geturl(tag['src'], downurl), path, downpath + '/'))
                    # res = res.replace(tag['src'], utils.getFileNameOrRename('/js/', tag['src']))

    return res
