#分类网页解析
#2020-8-5 评论中添加图片,根据图片名称列表，图片放在和exe文件同一目录下，支持jpg和png

import requests
from bs4 import BeautifulSoup 
import time
import re
from selenium import webdriver
import comment_dmzj as dmzj

# classFirstUrl="http://manhua.dmzj.com/tags/category_search/0-0-0-all-0-1-0-1.shtml#category_nav_anchor"  

url1 = "http://manhua.dmzj.com"

class IllegalException(Exception):
    '''
    Custom exception types
    '''
    def __init__(self, parameter, para_value):
        err = 'The parameter "{0}" is not legal:{1}'.format(parameter, para_value)
        Exception.__init__(self, err)
        self.parameter = parameter
        self.para_value = para_value

def getHtml(url):
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text 
    except:
        return "产生异常,url="+url

commicUrl = "http://manhua.dmzj.com/zaiyishijiebushibaideyibaizhongfangfa"

#soup.find(id="xx") 查找文档发现BeautifulSoup 可以根据属性查找tag
def getHrefCommentId(commicUrl):
    html = getHtml(commicUrl)
    soup = BeautifulSoup(html, "html.parser")
    subTag2s = soup.find(id="subscribe_id")
    if subTag2s:
        subTag3 = subTag2s.get("onclick")
        print(subTag3)
        comIdStr = re.search(r"\d+", subTag3).group(0)
        print(comIdStr)
        return comIdStr
    else: 
        raise IllegalException(commicUrl,"subscribe_id")

def getClassPageCommicIdSet(classFirstUrl, context, interval, imagineNameList):
    driver = webdriver.Chrome() 
    driver.get(classFirstUrl)
    time.sleep(1)
    html=driver.page_source
    driver.close()
    soup1=BeautifulSoup(html,'html.parser')
    subTag_block = soup1.find_all("div", "tcaricature_block tcaricature_block2")
    url_num = 0
    for subTag in subTag_block:
        subTag2 = subTag.find_all("ul")
        # urlSet = []
        acookieNo = 0
        for url in subTag2:
            subTag3 = url.find("a")
            if subTag3 and subTag3.get("target") == "_blank":
                subTag4 = subTag3.get("href")
                url_num = url_num + 1
                if re.search(r'.html', subTag4):
                    try:
                        id = getHrefCommentId(commicUrl)
                        dmzj.commentFunc(id, context, interval, acookieNo, imagineNameList)
                        acookieNo = acookieNo + 1
                    except IllegalException:
                        print("exception IllegalException, commicUrl=", commicUrl)
                    
                else: 
                    subTag5 = subTag4[0:len(subTag4)-1]
                    constructUrl = url1 + subTag5
                    #print(constructUrl)
                    try:
                        id = getHrefCommentId(constructUrl)
                        dmzj.commentFunc(id, context, interval, acookieNo, imagineNameList)
                        acookieNo = acookieNo + 1
                    except IllegalException:
                        print("exception IllegalException, constructUrl=", constructUrl)
    print("url num=", url_num)


def getAllPageUrlFunc(classFirstUrl, context, startPageNo, limitMaxPage, interval, imagineNameList):
    driver = webdriver.Chrome() 
    driver.get(classFirstUrl)
    time.sleep(1)
    html=driver.page_source
    driver.close()
    #print(html)
    soup = BeautifulSoup(html, "html.parser")
    t_minPage = 1
    print("##########################fount", soup.find("span", "font14black"))
    maxPageStr = soup.find("span", "font14black").string
    print("maxPageStr=", maxPageStr)
    t_maxPage = int(re.search(r'\d+', maxPageStr).group(0))
    if limitMaxPage:
        t_maxPage = min(t_maxPage, int(limitMaxPage))
    if startPageNo and startPageNo != "" :
        t_minPage = max(int(startPageNo), 1)
    print("t_maxPage", t_maxPage, "minPage=", t_minPage)
    #遍历分类页获取动漫url和对应id
    while t_minPage <= int(t_maxPage):
        constructUrl = re.sub(r'\d+.shtml', str(t_minPage) + ".shtml", classFirstUrl)
        print("constructUrl=", constructUrl, "t_minPage=", t_minPage, "context=", context)
        getClassPageCommicIdSet(constructUrl, context, interval, imagineNameList)
        t_minPage = t_minPage + 1



