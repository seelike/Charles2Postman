# -*- coding: utf-8 -*-

import json
import os

path = "/Users/lvxiran/bjhl/git/Charles2Postman/batchFile/"
targetPath = '/Users/lvxiran/bjhl/git/Charles2Postman/File/'


# 读取文件夹下的文件
def listDir():
    files = os.listdir(path);
    for oneFile in files:
        operateFile(oneFile)


# 解析单个文件
def operateFile(oneFile):
    print(type(oneFile))
    fullPath = path + oneFile
    fp = open(fullPath, 'r')
    json_data = json.load(fp)
    for i, oneJson in enumerate(json_data):
        list = []
        fullPath = targetPath + 'test' + str(i) + '.chlsj'
        new_file = open(fullPath, 'w')
        list.append(oneJson)
        new_file.write(json.dumps(list))
        new_file.close()
    print('这是文件中的json数据：', type(json_data))

if __name__ == '__main__':
    listDir()


# 读取json文件内容,返回字典格式
# with open('/Users/lvxiran/bjhl/git/Charles2Postman/batchFile/test00.json', 'r') as fp:
#     json_data = json.load(fp)
#     targetPath = '/Users/lvxiran/bjhl/git/Charles2Postman/File/'
#     for i, oneJson in enumerate(json_data):
#         list = []
#         fullPath = targetPath + 'test' + str(i) + '.chlsj'
#         new_file = open(fullPath, 'w')
#         list.append(oneJson)
#         new_file.write(json.dumps(list))
#         new_file.close()
#     print('这是文件中的json数据：',type(json_data))

