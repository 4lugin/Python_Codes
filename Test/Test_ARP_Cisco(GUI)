# -*- coding: utf-8 -*-

from Tkinter import *
import subprocess
import tkFileDialog
import tkMessageBox
import re
import shutil
import os

a = Tk()
a.title("hm...테스트")
config_path = 0
ip_path = 0


def link_1():
##    tkMessageBox.showinfo("Open Config_File","만드는중1..")
##    config_path = tkFileDialog.askopenfilename(initialdir = "./", title="파일열기", filetypes=("log files","*.log"))
    global config_path
    config_path = tkFileDialog.askopenfilename()
    config_path = os.path.splitext(config_path)[0]
    txt1.insert(0,config_path)

def link_2():
    global ip_path
    ip_path = tkFileDialog.askopenfilename()
    ip_path = os.path.splitext(ip_path)[0]
    txt2.insert(0,ip_path)

def b1_event():
## File Link
    n=0
    m=0
    file_arp = ip_path+".log"
    file_save = ".\\acl_result%d.log" %n
    file_origin = config_path+".log"
    file_result = ".\\Result.log"


    file = open(file_result, "w")
    file.close()
    os.unlink(file_result)


    ## First Loop
    c_arp = open(file_arp, "r")
    c_lines = c_arp.readlines()
    c_lines = list(map(lambda s: s.strip(), c_lines))
    c_arp.close()
    key = int(len(c_lines))

    a_acl = open(file_origin, "r")
    a_lines = a_acl.readlines()
    a_acl.close()


    for line in a_lines:
    	a = line.find(c_lines[0])
    	if (a == -1):
    		b = line
    		filter = open(file_save, "a")
    		filter.writelines(b)
    		filter.close()


    ## Seconds Loop
    while n < key-1:
    	k=n+1
    	file_origin = ".\\acl_result%d.log" %n
    	file_save = ".\\acl_result%d.log" %k

    	c_arp = open(file_arp, "r")
    	c_lines = c_arp.readlines()
    	c_lines = list(map(lambda s: s.strip(), c_lines))
    	c_arp.close()

    	a_acl = open(file_origin, "r")
    	a_lines = a_acl.readlines()
    	a_acl.close()

    	for line in a_lines:
    		a = line.find(c_lines[k])

    		if (a == -1):
    			b = line
    			filter = open(file_save, "a")
    			filter.writelines(b)
    			filter.close()


    	os.unlink(file_origin)
    	n +=1


    ## Final
    shutil.copy(file_save, file_result)
    os.unlink(file_save)

    tkMessageBox.showinfo("Finish","추출 완료!!")
    print ("\n\n   :::: Success !! ::::\n")


def re_1():
    subprocess.call(("notepad.exe","./Result.log"))

t_menu = Menu(a)
a.config(menu = t_menu)

t_acl = Menu()
t_acl.add_command(label="Open_Result", command=re_1)
t_menu.add_cascade(label="Result", menu = t_acl)




m1 = "[ASA-FW] IP Filterling\n\n 모든 파일은 .log 로 저장할 것!!"
label1 = Label(a, text = m1)
label1.pack(side=TOP, padx = 10, pady = 100)

txt1 = Entry(a, width=30)
txt1.pack()
btn1 = Button(a, width=30, text="1. Config_File", command=link_1)
btn1.pack(side=TOP, padx = 10)


txt2 = Entry(a, width=30)
txt2.pack()
btn2 = Button(a, width=30, text="2. Delete_Ip_File", command=link_2)
btn2.pack()

## Run

btn3 = Button(a, width=20, height=5, bg="gray", text="RUN", command=b1_event)
btn3.pack(side=BOTTOM, pady = 20)


a.mainloop()
