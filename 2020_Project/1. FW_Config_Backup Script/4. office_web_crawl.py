#-*- coding: utf-8 -*-
# -------------------------------------
# Date: 2020.06.12
# Made by Young-ho Kim
# -------------------------------------
# platform : Windows 10
# Language : Python 3.6
# Modules :
# pip3 install Paramiko --trusted-host pypi.org --trusted-host files.pythonhosted.org
# pip3 install --upgrade certifi
# pip3 install --upgrade pyasn1
# pip3 install pyOpenSSL
# pip3 install ndg-httpsclient
# -------------------------------------

import sys
import os
import shutil    ## 파일이동
import requests
import time
import datetime
import re       ## 정규식 모듈


##---------------------------------------------------------------
## Disable flat warning_ SSL 관련 에러 출력 끔
requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

## TLSv1_ TLS_RSA_WITH_3DES_CBC_SHA 설정
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += (':DES-CBC3-SHA')
##---------------------------------------------------------------


## ID/PW 계정 암호화 값_ Fiddler 패킷 캡쳐로 실제 웹 로그인 후 Payload 복사
login_un = 'xxxxxxxxx='
login_pw = 'xxxxxxxxx='

## url
url = 'https://1.1.1.1/index.html'

## Default Setting
conn_count = 0    ## save_list 리스트 순서 카운트용
dir = './config/' ## 저장경로

if not os.path.exists(dir):   ## 저장 디렉토리 없을경우 생성
    os.mkdir(dir)

## File Reset
file_save = dir+'test_1.1.1.1_web.log'
file = open(file_save, 'w'. encoding='utf-8')
file.close()


## time
ti = str(int((datetime.datetime.utcnow() - datetime.datetime(1970,1,1)).total_seconds()*1000))
login_time = ti[4:]

## 로그인시 Payload
login_payload = {
'admin_id': '',
'admin_pw': '',
'time': login_time,
'un': login_un,
'pw': login_pw
}

## Session Connection
s = requests.Session()
login_req = s.post(url, data=login_payload, verify=False, allow_redirects=True)  ## verify=False는 인증서 오류 무시
location_url = login_req.history[0].headers['Location']    ## Loacation 에 sid가 포함된 url
sid = location_url.split('=')  ## sid 추출

## config 출력되는 페이지 접근
config_url = 'https://1.1.1.1/'+sid[1]+'/cfg_file_cfg_cnt.html'
config_req = s.get(config_url, verify=False)  ## config 페이지요청
config_req.encoding = 'euc-kr'   ## 한글 깨짐현상 해결
config_html = config_req.text
config_html_replace = config_html.replace('%quot;','"')  ## %quot; 문자 "로 치환

## config 구문만 분리
req = re.search('(?<=<TEXTAREA name="cfg_msg" readonly ROWS="12" COLS="80">)).*(?=</TEXT)'), config_html_replace, re.DOTALL)  ## re.DOTALL 을 해줘야 줄바꿈 문자까지 전부 출력가능
m = req.group()
print(m)


## 파일저장
fout = open(file_save, 'a', newline="", encoding='utf-8')
fout.writelines(m)
fout.close()


## END
print ('\n\n   :::: Success !! ::::\n')
