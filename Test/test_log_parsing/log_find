# platform : Windows 7
# Language : Python 3.6
# easy_install requests

#-*- coding: utf-8 -*-

import re

n = 0

## File Path
file_path = "./log.log"
result_path = "./log_result.log"

## Reset Result file
file = open(result_path, "w",encoding="utf-8")
file.close()

## Rex Keyword
findString = input(">> Find String?: ")

## Running
file = open(file_path, "r")
lines = file.readlines()
file.close()

for line in lines:
    u = re.findall(findString, line, re.I)

    timeMethod = "[0-9]{2}:[0-9]{2}:[0-9]{2}"
    com_1 = re.findall(timeMethod, line, re.I)

    if len(u) > 0:
        result = open(result_path, "a",encoding="utf-8")
        result.writelines(line)
        print(line)
        n += 1

    elif len(com_1) > 0:
        n = 0

    elif n > 0:
        result = open(result_path, "a",encoding="utf-8")
        result.writelines(line)
        print(line)




print ("\n\n   :::: Success !! ::::\n")
