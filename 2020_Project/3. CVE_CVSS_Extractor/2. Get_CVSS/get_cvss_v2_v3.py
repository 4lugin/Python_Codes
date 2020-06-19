#-*- coding: utf-8 -*-
# -------------------------------------
# Date: 2019.04.16
# Made by Young-ho Kim
# -------------------------------------
# platform : Windows 10 (64bit)
# Language : Python 3.7.3
# pip3 install requests --trusted-host pypi.org --trusted-host files.pythonhosted.org
# pip3 install beautifulsoup4 --trusted-host pypi.org --trusted-host files.pythonhosted.org
# pip3 install cvss --trusted-host pypi.org --trusted-host files.pythonhosted.org
# -------------------------------------


import re           # 정규표현식
import shutil       # 파일 이동/복사
import os           # OS 기능사용
import requests     # http 요청
import bs4          # http 페이지 정보추출
import cvss         # cvss 모듈
requests.packages.urllib3.disable_warnings()    # requests 모듈 에러메세지 출력OFF

## File Path
file_cve = "./input_cve_result.log"
file_nvdTmp = "./temp_cve.log"
file_nvdTmp_v2 = "./temp_cve_v2.log"
file_out = "./[+]cvss3_result.log"

## File Reset
file = open(file_nvdTmp, "w")
file.close()
file = open(file_nvdTmp_v2, "w")
file.close()
file = open(file_out, "w")
file.close()


## Variable Reset
numCVE = "0"

## Define
def getCVE_detail():        # input_cve_result.log 파일에서 https://nvd.nist.gov 데이터 저장
    file = open(file_cve,"r",encoding="utf-8")   # temp_cve.log 로 저장
    lines = file.readlines()
#    lines.remove("\n")  # input_cve_result.log 첫번째 줄 리스트에서 제거
    file.close()
    lines = list(map(lambda s: s.strip(), lines))   # \n 문자열 제거

    ssl_url = "https://nvd.nist.gov"
    ssl_con = requests.get(ssl_url, verify=False)

    for line in lines:
        global numCVE
        numCVE = line

        url = "https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?name="+line
        res = requests.get(url, verify=False)

        url_v2 = "https://nvd.nist.gov/vuln-metrics/cvss/v2-calculator?name="+line
        res_v2 = requests.get(url_v2, verify=False)

        get_nvdCVE = open(file_nvdTmp,"w", encoding="utf-8")
        get_nvdCVE.write(res.text)
        get_nvdCVE.close()

        get_nvdCVE_v2 = open(file_nvdTmp_v2,"w", encoding="utf-8")
        get_nvdCVE_v2.write(res_v2.text)
        get_nvdCVE_v2.close()

        PageRegex = re.compile(r'Warning: Unable to find vulnerability requested')
        chkPage = PageRegex.search(res.text)
        chkPage_v2 = PageRegex.search(res_v2.text)


        try:
                chkPage_v2.group()
                print('[-]'+line+' -> [ERROR] Not found v2 CVE database')

                chkPage.group()
                print('[-]'+line+' -> [ERROR] Not found v3 CVE database')


        except:
            try:
                file = open(file_nvdTmp, encoding="utf-8") # 데이터는 [+]cvss3_result.log 로 저장
                file_v2 = open(file_nvdTmp_v2, encoding="utf-8")

                htmlParser = bs4.BeautifulSoup(file.read(),"html.parser")
                htmlParser_v2 = bs4.BeautifulSoup(file_v2.read(),"html.parser")
                file.close()
                file_v2.close()

                a = htmlParser.find_all('div',id='p_lt_WebPartZone1_zoneCenter_pageplaceholder_p_lt_WebPartZone1_zoneCenter_CVSSV3Calculator_FormPanel')
                a2 = re.findall("(?<=value=\")[a-zA-Z:/]{20,40}",str(a))
                b = cvss.CVSS3("CVSS:3.0/"+a2[0])
                b2 = b.scores()
                c = b.severities()

                a_v2 = htmlParser_v2.find_all('div',id='p_lt_WebPartZone1_zoneCenter_pageplaceholder_p_lt_WebPartZone1_zoneCenter_CVSSV2Calculator_FormPanel')
                a2_v2 = re.findall("(?<=value=\"\()[a-zA-Z:/]{20,40}",str(a_v2))
                b_v2 = cvss.CVSS2(a2_v2[0])
                b2_v2 = b_v2.scores()


                saveFile = open(file_out,"a")
                #saveFile.write(numCVE+', Score(v3)= '+str(b2[0])+', Impact CIA= '+str(c)+"\n")
                #saveFile.write(numCVE+', Score(v3/v2)= '+str(b2[0])+'/'+str(b2_v2[0])+', Impact CIA(v3)= '+str(c)+'\n')
                saveFile.write(numCVE+','+str(b2[0])+','+str(b2_v2[0])+','+str(c[0])+','+str(c[1])+','+str(c[2])+'\n')

                saveFile.close()

                print('[+]'+line+' -> Score(v3/v2)= '+str(b2[0])+'/'+str(b2_v2[0])+' / '+str(c[0])+','+str(c[1])+','+str(c[2]))


            except IndexError:
                print('[-]'+line+' -> [ERROR] Not CVSS Vector')







##################################################################
# Running
##################################################################
print ("\n-----------------------------------------------------------------------------------")
print ("\n[ API Server - https://nvd.nist.gov (CVSS v3) ]\n")
print ("-----------------------------------------------------------------------------------\n")

getCVE_detail()

print ("\n-----------------------------------------------------------------------------------")
print ("\n\n   :::: Success !! ::::\n")
