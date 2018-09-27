# platform : Windows 7
# Language : Python 3.6
# pip install cymruwhois

#-*- coding: utf-8 -*-


import sys
import re
import socket
from cymruwhois import Client
import os           # OS 기능사용
import requests     # http 요청
requests.packages.urllib3.disable_warnings()    # requests 모듈 에러메세지 출력OFF
import json


## ip.log File Open
file_name = "./ip"
file_path = file_name +".log"
save_detail = "./ip_detail.log"
save_file = "./ip_result.log"

## ip_result.log Reset
file = open(save_detail, "w",encoding="utf-8")
file.writelines("\n[ API Server - whois.cymru.com ]\n")
file.writelines("-----------------------------------------------------------------------------------\n")
file.writelines("[*]\t[Search IP]\t[Cymru/KISA]\t[AS Name]\n")
file.writelines("-----------------------------------------------------------------------------------\n")
file.close()

file = open(save_file, "w",encoding="utf-8")
file.close()


ip_file = open(file_path, "r")
ip_lines = ip_file.readlines()
ip_lines = list(map(lambda s: s.strip(), ip_lines))
ip_file.close()
ip_cnt = int(len(ip_lines))


## Running
print ("\n[ API Server - whois.cymru.com ]")
print ("-----------------------------------------------------------------------------------")
print ("[*]\t[Search IP]\t[Cymru/KISA]\t[AS Name]")
print ("-----------------------------------------------------------------------------------")

for line in ip_lines:
    ip = socket.gethostbyname(line)
    c=Client()
    r=c.lookup(ip)
    a=r.owner
    f=re.findall("[A-Z]{2}", a)
    c=len(f)

    url = "http://whois.kisa.or.kr/openapi/whois.jsp?query="+line+"&key=2018052409355407130895&answer=json"
    res = requests.get(url, verify=False)
    dict = json.loads(res.text)


    if f[c-1] == "KR":
        kr_chk = "Korea"
        '''
        whois = open(save_file, "a",encoding="utf-8")
        whois.writelines("[Korea]\n")
        whois.close()
        '''

        whois = open(save_detail, "a",encoding="utf-8")
        whois.writelines(kr_chk+"\t"+line+"\t  "+f[c-1]+"\t"+dict['whois']['countryCode']+"\t"+r.owner+"\n")
        whois.close()


    else:
        kr_chk = " "
        '''
        whois = open(save_file, "a",encoding="utf-8")
        whois.writelines(f[c-1]+"\n")
        whois.close()
        '''

        whois = open(save_detail, "a",encoding="utf-8")
        whois.writelines(kr_chk+"\t"+line+"\t  "+f[c-1]+"\t"+dict['whois']['countryCode']+"\t"+r.owner+"\n")
        whois.close()
    print (kr_chk+"\t"+line+"\t  "+f[c-1]+"\t"+dict['whois']['countryCode']+"\t"+r.owner)

print ("-----------------------------------------------------------------------------------\n")




## Kisa Whois API
'''
for line in ip_lines:
    url = "http://whois.kisa.or.kr/openapi/whois.jsp?query="+line+"&key=2018052409355407130895&answer=json"
    res = requests.get(url, verify=False)

    whois = open(save_detail, "a",encoding="utf-8")
    whois.write(line+"\t"+res.text)
    whois.close()


    dict = json.loads(res.text)
    print (dict['whois']['countryCode'])
'''


file = open(save_detail, "a",encoding="utf-8")
file.writelines("-----------------------------------------------------------------------------------\n")
file.close()
