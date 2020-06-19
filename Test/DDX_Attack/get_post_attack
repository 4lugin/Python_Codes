#-*- coding: utf-8 -*-
﻿# platform : Windows 7
# Language : Python 3.6
# pip3 install requests --trusted-host pypi.org --trusted-host files.pythonhosted.org


import os
import requests
import time
requests.packages.urllib3.disable_warnings()

## Loop n_count
op = input(">> get/post?: ")

#a_url = ""
a_url = input(">> URL (ex. http://test.com): ")
cNum = int(input(">> Total Send Packet?: "))
tNum = int(input(">> Send Packet Count Per Second: "))

def test_get():
    n=1
    while n < cNum+1:
        try:
           res = requests.get(a_url, timeout=1/tNum, verify=False)
           print ("\nGET Packet Count:",n,"(Connect Success!!)")
           print (time.strftime('%Y/%m/%d %H:%M:%S', time.localtime()))
           n = n+1

        except requests.exceptions.Timeout:
            print ("\nGET Packet Count:",n,"(Disconnect)")
            print (time.strftime('%Y/%m/%d %H:%M:%S', time.localtime()))
            n = n+1


def test_post():
    n=1
    while n < cNum+1:
        try:
            res = requests.post(a_url, timeout=1/tNum, verify=False)
            print ("\nPOST Packet Count:",n,"(Connect Success!!)")
            print (time.strftime('%Y/%m/%d %H:%M:%S', time.localtime()))
            n = n+1

        except requests.exceptions.Timeout:
            print ("\nPOST Packet Count:",n,"(Disconnect)")
            print (time.strftime('%Y/%m/%d %H:%M:%S', time.localtime()))
            n = n+1



while(op == "get"):
    test_get()
    break

while(op == "post"):
    test_post()
    break

print ("\n\n   :::: Success !! ::::\n")
