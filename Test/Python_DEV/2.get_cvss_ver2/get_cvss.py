#-*- coding: utf-8 -*-

# -------------------------------------
# Date: 2018.06.07
# Made by Young-ho Kim
# -------------------------------------
# platform : Windows 7 (64bit)
# Language : Python 3.6
# easy_install requests
# easy_install beautifulsoup4
# -------------------------------------


import re           # 정규표현식
import shutil       # 파일 이동/복사
import os           # OS 기능사용
import requests     # http 요청
import bs4          # http 페이지 정보추출
requests.packages.urllib3.disable_warnings()    # requests 모듈 에러메세지 출력OFF


## Path Files
file_cve = "./input_cve_result.log"
file_cvedetail = "./temp_cve.log"
file_fil = "./[+]cvss_result.log"
nCVE = "0"


## File Reset
file = open(file_cvedetail, "w")
file.close()
file = open(file_fil, "w")
file.close()
os.unlink(file_cvedetail)
os.unlink(file_fil)


## Define
def getCVE_detail():        # input_cve_result.log 파일에서 cvedetails.com 데이터 저장
    file = open(file_cve,"r",encoding="utf-8")   # temp_cve.logg 로 저장
    lines = file.readlines()
#    lines.remove("\n")  # input_cve_result.log 첫번째 줄 리스트에서 제거
    file.close()
    lines = list(map(lambda s: s.strip(), lines))   # \n 문자열 제거

    ssl_url = "https://www.cvedetails.com"
    ssl_con = requests.get(ssl_url, verify=False)

    for line in lines:
        global nCVE
        nCVE = line

        url = "https://www.cvedetails.com/cve-details.php?cve_id="+line
        res = requests.get(url, verify=False)
        get_deCVE = open(file_cvedetail,"w", encoding="utf-8")
        get_deCVE.write(res.text)
        get_deCVE.close()

        if ( len(res.text) < 20000):
            print (len(res.text),nCVE+"  찾을 수 없음")
            continue
        else:
            print (len(res.text),nCVE+"  기록완료!!")
            fil_cve()


def fil_cve():                  # temp_cve.log 파일에서 4가지 추출
    file = open(file_cvedetail) # 데이터는 [+]cvss_result.log 로 저장
    soupData = bs4.BeautifulSoup(file.read(),"html.parser")
    file.close()

    try:
        a = str(soupData.find_all("table", {"class":"details"}))
        a2 = re.findall("\>([0-9]{1,2}\.[0-9]{1})",a)
        b = str(soupData.find_all("table", {"class":"details"}))
        b2 = re.findall("\"\>([a-zA-Z]{4,8})\<",b)

        saveFile = open(file_fil,"a")
        saveFile.write(nCVE+','+a2[0]+','+b2[0]+','+b2[1]+','+b2[2]+"\n")
        saveFile.close()

    except IndexError:
        print (nCVE+"  (CVSS값 없음) Index Error")



##################################################################
# Running
##################################################################
getCVE_detail()

print ("\n\n   :::: Success !! ::::\n")
