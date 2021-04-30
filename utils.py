import requests
import re
from urllib.parse import urlparse
import os
import random


# 下载文件
def download_file(url, path, savepath):
    print('下载文件:' + url)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE"}
    r = requests.get(url, headers=headers)

    name = getFileName(url)
    name2 = path + '/' + savepath + getFileName(url)
    name3 = reFileName(name)
    print(name3)
    if ifHasSameFile(name2):
        with open(path + '/' + savepath + name3, "wb") as code:
            code.write(r.content)
        return savepath + name3
    else:
        with open(name2, "wb") as code:
            code.write(r.content)
        return savepath + name


# 判断是否有同名文件
def ifHasSameFile(path):
    if os.path.exists(path):
        return True
    else:
        return False


# 获取文件名
def getFileName(s):
    str = re.findall(r'[^/]+(?!.*/)', s)[0]
    head, sep, tail = str.partition('?')
    return head


# 判断文件是否存在存在则重命名
def getFileNameOrRename(path, name):
    filename = getFileName(name)
    if ifHasSameFile(path + filename):
        return reFileName(path + filename)
    else:
        return path + filename


def reFileName(s):
    head, sep, tail = s.partition('.')
    name = head + generate_random_str(5) + sep + tail
    return name


# 生成随机字符串
def generate_random_str(randomlength=16):
    """
    生成一个指定长度的随机字符串
    """
    random_str = ''
    base_str = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789'
    length = len(base_str) - 1
    for i in range(randomlength):
        random_str += base_str[random.randint(0, length)]
    return random_str


# 域名处理
def geturl(s, downurl):
    if (urlparse(s).netloc):
        if (urlparse(s).scheme):
            return urlparse(s).scheme + '://' + urlparse(s).netloc + urlparse(s).path
        else:
            return 'http://' + urlparse(s).netloc + urlparse(s).path
    else:
        return urlparse(downurl).scheme + '://' + urlparse(downurl).netloc + '/' + s


def makedir(path):
    if not os.path.exists(path):
        os.mkdir(path)
