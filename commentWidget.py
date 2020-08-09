
#修改 ： 2020-8-5 评论中添加图片,根据图片名称列表，图片放在和exe文件同一目录下，支持jpg和png
import sys
import comment_dmzj as dmzj
import passer2 as passer  
import time
import random 
import os 
import file 

#读取文件cookies,更新评论模块的cookie
cookiesSet = []
if file.getCookiesFromFile('cookies.txt', cookiesSet):
    dmzj.cookieSet = cookiesSet
else:
    print("读取cookies文件错误")
    os.system("pause")

classUrl = input("输入选好的分类界面的地址（http...）\n")
comment = input("输入评论内容(字符串)\n")
interval = float(input("输入评论时间间隔(数字)\n"))
minPageNo= int(input("输入评论起始的页数（数字）\n"))
maxPageNo = int(input("输入评论到的页数（数字）\n"))


imagineNum = int(input("输入评论图片数量（0~3）\n"))
imagineNameList = []
if imagineNum > 3 or imagineNum < 0:
    print("输入图片数量错误")
    os.system("pause")
num = 1
while num <= imagineNum:
    imagineName = input("输入第" + str(num) + "张图片文件名（xxx.png或者xxx.jpg）\n")
    imagineNameList.append(imagineName) 
    num = num + 1

passer.getAllPageUrlFunc(classUrl, comment, minPageNo, maxPageNo, interval, imagineNameList)

print("已经完成评论！\n")
print("\n")

os.system("pause")






