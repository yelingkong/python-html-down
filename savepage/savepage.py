# coding=utf-8

def savepage(res, files):
    file = open(files, 'w',encoding='utf-8')
    file.write(res)
    file.close()
