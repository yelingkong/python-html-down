# coding=utf-8

def savepage(res, files):
    file = open(files, 'w')
    file.write(res)
    file.close()
