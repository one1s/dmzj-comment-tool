#ccj 2020.8.5 图片上传模块（评论中添加图片）
import requests
from bs4 import BeautifulSoup 
import re 

cookie = "UM_distinctid=17220d4778a24b-03dfa2bfa5dc9e-376b4502-15f900-17220d4778b155; show_tip_1=0; show_tip=0; RORZ_7f25_ulastactivity=c322XvtUc1kT8xOqe2DOPZtYS3aS2GxuCXy5jRPxr%2BTHweyH5loP; pt_198bb240=uid=nfTTy4ekNMrYXVq860TRSA&nid=0&vid=hF6X7WUAVaOfAipN2hqCGg&vn=8&pvn=1&sact=1590938152508&to_flag=0&pl=nNm-nGOhZFGdV9qHmfngNQ*pt*1590938149419; love=cb0d92a7b8d377b85381d5a4772f9d72; BAIDU_SSP_lcr=https://www.so.com/link?m=boRqDJUGIqDedcNL3tl2g4Mo%2BlHF7%2F4wP4VQFe63vBkX8dfT2NGqEp1glFqV1nan3Y%2Bnpo8OIaHx3vNp6WQUTMox8cSbtvAqrmtA%2BSauLTL89%2BdT6bl328QZtEJbQkyDDb7uHtxTYz1Xav%2Bp2; KLBRSID=b70234c3735a733fd08ac86b286a9331|1596603940|1596593474"

def getImgineName(cookie, filename):
    url = "http://interface.dmzj.com/api/NewComment2/addImg?cb=http://manhua.dmzj.com/images/conmment_cd.html"
    cookie = {'cookie': cookie}
    agent  = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:17.0; Baiduspider-ads) Gecko/17.0 Firefox/17.0"
    header = {'User-Agent': agent}
    files = None
    try:
        files  = {'userfile[]':(filename, open(filename, 'rb'), 'image/png')}
    except: 
        print("打开图片文件失败,请检查文件名是否正确，fileName=", filename)
        os.system("pause")
    res = requests.request("POST", url, cookies = cookie, files = files, headers = header)
    print(res.text)
    matchObj = re.search(r'\d+.\d+.(jpg|png)', res.text)
    if matchObj:
        return matchObj.group(0)
    else:
        return ""

def getImagineStrByList(cookie, rawFileNameList):
    resNameStr = ""
    for fileName in rawFileNameList:
        if fileName and fileName != "":
            resName = getImgineName(cookie, fileName)
            print("resName=", resName)
            if resName and resName != "":
                if resNameStr != "":
                    resNameStr = resNameStr + "," + resName 
                else: 
                    resNameStr = resNameStr + resName 
    print("getImagineStrByList done, resNameStr=", resNameStr)
    return resNameStr 

#rawFileNameList = {"rules.jpg", "second1.png"}
#getImgineName(cookie, "rules.jpg")
#getImagineStrByList(cookie, rawFileNameList)
#getImgineName(cookie, "rules.jpg")


