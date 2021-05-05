import requests
import re
from urllib.parse import urlparse
import os
import random
import hashlib


# 下载文件
def download_file(url, path, savepath, downurl):
    print('下载文件:' + url)
    makedir(path + '/' + savepath)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE",
        "Referer": downurl
    }
    r = requests.get(url, headers=headers)

    name = getFileName(url)
    name2 = path + '/' + savepath + getFileName(url)
    name3 = reFileName(name)
    # 判断是否有重名文件
    if ifHasSameFile(name2):
        with open(path + '/' + savepath + name3, "wb", encoding='utf-8-sig') as code:
            code.write(r.content)
            # 判断是否需要删除新文件
        if ifNeedDelete(name2, path + '/' + savepath + name3):
            return savepath + name
        else:
            return savepath + name3
    else:
        with open(name2, "wb", encoding='utf-8-sig') as code:
            code.write(r.content)
        return savepath + name


def getHash(f):
    line = f.readline()
    hash = hashlib.md5()
    while (line):
        hash.update(line)
        line = f.readline()
    return hash.hexdigest()


def IsHashEqual(f1, f2):
    str1 = getHash(f1)
    str2 = getHash(f2)
    return str1 == str2


def ifNeedDelete(f1, f2):
    f1s = open(f1, "rb", encoding='utf-8-sig')
    f2s = open(f2, "rb", encoding='utf-8-sig')
    if IsHashEqual(f1s, f2s):
        os.remove(f2)
        return True
    else:
        return False


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


def Handlefile(nameurl, path, downurl):
    file = open(path + '/' + nameurl, 'r', encoding='utf-8-sig')
    content = file.read()
    file.close()
    rs = re.findall('url\((\S*)\)', content, re.S)
    for item in rs:
        if bool(re.search('data:', item)):
            print('base64图片不需要下载')
        elif bool(re.search('../', item)):
            download_file(geturl(replacex(item), downurl), path, 'images/', downurl)
        else:
            item = replacex(item)
            download_file(geturl(replacex(item), downurl), path, 'images/', downurl)


# 下载页面内css的背景图片
def downCssbg(content, path, downurl):
    rs = re.findall('url\((\S*)\)', content, re.S)
    for item in rs:
        if bool(re.search('data:', item)):
            print('base64图片不需要下载')
        elif bool(re.search('../', item)):
            content = content.replace(item, download_file(geturl(replacex(item), downurl), path, 'images/', downurl))
        else:
            item = replacex(item)
            content = content.replace(item, download_file(geturl(replacex(item), downurl), path, 'images/', downurl))
    return content



def replacex(str):
    data = ['../', '"', '\'']
    str2 = str
    for item in data:
        str2 = str2.replace(item, '', 100)
    return str2
