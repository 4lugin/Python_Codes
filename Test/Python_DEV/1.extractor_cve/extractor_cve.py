#-*- coding: utf-8 -*-

# -------------------------------------
# Date: 2018.06.07
# Made by Young-ho Kim
# -------------------------------------
# platform : Windows 7 (64bit)
# Language : Python 3.6
# -------------------------------------


import re

## Path Files
file_origin = ".\\input_cve.log" # UTF-8 save
file_save = ".\\input_cve_result.log"

## Reset & Banner
file = open(file_save, "w",encoding="utf-8")
##file.writelines("##### Result #####\n")
file.close()

## Rex Keyword
file = open(file_origin, "r",encoding="utf-8")
lines = file.readlines()
file.close()

for line in lines:
        p = re.findall("CVE-[0-9]{4}-[0-9]{0,10}", line, re.I) ## new rex
        cve = open(file_save, "a",encoding="utf-8")
        cve.writelines(p)
        cve.close()

## Line add \n
file = open(file_save, "r",encoding="utf-8")
data = file.read()
file.close()

file = open(file_save, "w",encoding="utf-8")
file.write(data.replace("CVE","\nCVE"))
file.close()

## Last Line add \n
file = open(file_save, "a",encoding="utf-8")
file.write("\n")
file.close()



## Remove duplicates
file = open(file_save, "r",encoding="utf-8")
lines = file.readlines()
file.close()

result = []
for i in lines:
    if i not in result:
        result.append(i)

file = open(file_save, "w",encoding="utf-8")
file.writelines(result)
file.close()


print ("\n\n   :::: Success !! ::::\n")
