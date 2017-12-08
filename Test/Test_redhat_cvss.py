#-*- coding: utf-8 -*-
# platform : Windows 7
# Language : Python 3.6
# easy_install requests
# easy_install beautifulsoup4

import re           # 정규표현식
import shutil       # 파일 이동/복사
import os           # OS 기능사용
import requests     # http 요청
import bs4          # http 페이지 정보추출
requests.packages.urllib3.disable_warnings()    # requests 모듈 에러메세지 출력OFF

# File Link Address
file_temp = "./0_redtemp.log"
file_cve = "./1_cve.log"
file_cvedetail = "./2_cvedetail.log"
file_fil = "./3_redhat_end.log"
nCVE = "0"

# File Reset
file = open(file_temp, "w")
file.close()
file = open(file_cve, "w")
file.close()
file = open(file_cvedetail, "w")
file.close()
file = open(file_fil, "w")
file.close()
os.unlink(file_temp)
os.unlink(file_cve)
os.unlink(file_cvedetail)
os.unlink(file_fil)


# Define
def getCVE_redhat():        # redhat api 에서 데이터 가져오기(0_redtemp.log에 저장)
    selDate = input(">>Search Date(ex. 2017-01-01): ") # 해당날짜 이후로 CVE Data 추출
    url = "https://access.redhat.com/labs/securitydataapi/cve?after="+selDate
    res = requests.get(url, verify=False)
    get_temp = open(file_temp,"w",encoding="utf-8")
    get_temp.write(res.text)
    get_temp.close()


def findCVE():          # 0_temp.log 파일에서 cve값 추출(1_cve.log에 저장)
    tempFile = open(file_temp,"r")
    lines = tempFile.readlines()
    tempFile.close()

    for line in lines:
        findCVE = re.findall("\"([CVE-]+[0-9]{4}\-[0-9]{0,10})", line, re.I)
        cve = open(file_cve, "a")
        cve.writelines(findCVE)
        cve.close()

    tempFile = open(file_cve, "r")
    data = tempFile.read()
    tempFile.close()
    tempFile = open(file_cve, "w")
    tempFile.write(data.replace("CVE","\nCVE"))
    tempFile.close()


def getCVE_detail():        # 1_cve.log 파일에서 cvedetails.com 데이터 저장
    file = open(file_cve,"r")   # 데이터는 2_cvedetail.log 로 저장
    lines = file.readlines()
    lines.remove("\n")  # 1.cve.log 에 있는 첫번째 줄 리스트에서 제거
    file.close()
    lines = list(map(lambda s: s.strip(), lines))   # \n 문자열 제거
    print(lines)

    for line in lines:
        global nCVE
        nCVE = line
        url = "https://www.cvedetails.com/cve-details.php?cve_id="+line
        res = requests.get(url, verify=False)
        get_deCVE = open(file_cvedetail,"w", encoding="utf-8")
        get_deCVE.write(res.text)
        get_deCVE.close()
        print (len(res.text))

        if ( len(res.text) < 20000):
            #saveFile = open(file_fil,"a")
            #saveFile.write(line+',''Not Found...\n')
            #saveFile.close()
            continue
        else:
            #saveFile = open(file_fil,"a")
            #saveFile.write(line+',')
            #saveFile.close()
            fil_cve()


def fil_cve():                  # 2_result.log 파일에서 4가지 추출
    file = open(file_cvedetail) # 데이터는 3_end.log 로 저장
    soupData = bs4.BeautifulSoup(file.read(),"html.parser")
    file.close()

    try:
        a = str(soupData.find_all("table", {"class":"details"}))
        a2 = re.findall("\>([0-9]{1}\.[0-9]{1})",a)
        b = str(soupData.find_all("table", {"class":"details"}))
        b2 = re.findall("\"\>([a-zA-Z]{4,8})\<",b)

        saveFile = open(file_fil,"a")
        saveFile.write(nCVE+','+a2[0]+','+b2[0]+','+b2[1]+','+b2[2]+"\n")
        saveFile.close()

    except IndexError:
        #saveFile = open(file_fil,"a")
        #saveFile.write(nCVE+','+'Index Not Found...\n')
        #saveFile.close()
        print ("Index Error")



##################################################################
# Running
##################################################################
getCVE_redhat()
findCVE()
getCVE_detail()

print ("\n\n   :::: Success !! ::::\n")
