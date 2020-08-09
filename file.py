#把文件中的cookie转为列表并返回
import os 
import re 

def getCookiesFromFile(filePath, cookieSet):
    file = None
    try:
        file = open("cookies.txt", "r")
    except IOError:
        print("文件打开失败")
        return False 
    else: 
        print("文件打开成功")
        
    print(file)
    for text in file: 
        res = re.match(r'^.*\d+', str(text))
        if res: 
            cookieSet.append(res.group(0))
            print(res.group(0))
    file.close()
    return True 

def saveCookiesToFile(filePath, cookieSet):
    file = None
    try:
        file = open("cookies.txt", "w")
    except IOError:
        print("文件打开失败")
        return False 
    else: 
        print("文件打开成功")

    for cookie in cookieSet: 
        file.writelines(cookie+"\n")
    file.close()

    






