#-*- coding: utf-8 -*-
# -------------------------------------
# Date: 2020.06.08
# Made by Young-ho Kim
# -------------------------------------
# platform : Windows 10
# Language : Python 3.6
# pip3 install Paramiko --trusted-host pypi.org --trusted-host files.pythonhosted.org
# -------------------------------------

import sys
import paramiko
import time
import os        ## 디렉토리 생성용
import getpass   ## PW 안보이게 입력모듈

## Default Setting
conn_count = 0    ## save_list 리스트 순서 카운트용
dir = './config/' ## 저장경로

if not os.path.exists(dir):   ## 저장 디렉토리 없을경우 생성
    os.mkdir(dir)

host_list = [
'1.1.1.1',
'2.2.2.2'
]

save_list = [
dir+'test_1.1.1.1.log',
dir+'test_2.2.2.2.log'
]


## ID/PW input
port_num = '22'
useername = input('>> Username: ')
password = getpass.getpass('>> Password: ')

## File Reset
for file_save in save_list:
    file = open(file_save, 'w', encoding='utf-8')
    file.close()


## Main Running
for host in host_list:
    not_done = 1    ## 소켓 사이즈 오버플로우 분산저장 여부 체크용
    i = 0           ## 몇번째 recv 처리인지 카운트용

    ## Connection Session
    s_client = paramiko.SSHClient()
    s_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        s_client.connect(host, port_num, username, password)
    except:
        conn_count += 1
        print ('\n[ Session Connection Error {0} ]\n'.format(host))
    else:
        conn_client = s_client.invoke_shell()
        time.sleep(.5)
        output = conn_client.recv(65535)
        print ('\n[ Session Established with {0} ]\n'.format(host))

        ## juniper config
        conn_client.send('get config\n')
        time.sleep(2.5)

        ## Buffer Over Resolve
        while not_done:
            time.sleep(.5)
            i += 1
            if conn_client.recv_ready():
                output += conn_client.recv(65535)
                print ('[+] '+host+': Runnung '+'[',i,']'+' >> Data Size:'+len(output))
            else:
                not_done = False
                print ('[-] Total Size:', len(output), 'bytes\n')

        ## File save
        dataout = output.decode('euc-kr', 'ignore')
        fout = open(save_list[conn_count], 'a', newline="", encoding='utf-8')
        fout.writelines(dataout)
        fout.close()
        conn_count += 1
        s_client.close()

## END
print ('\n\n   :::: Success !! ::::\n')
