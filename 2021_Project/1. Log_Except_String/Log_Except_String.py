#-*- coding: utf-8 -*-
# -------------------------------------------
# Date: 2021.05.21
# Made by Young-ho Kim
# -------------------------------------------
# platform : Windows 10
# Language : Python 3.6
# -------------------------------------------

import re


## Path Files
p_infile = ".\\input.log"
p_outfile = ".\\result.log"


## File Reset
file = open(p_outfile, "w", encoding="utf-8")
file.close()


## Read File
file = open(p_infile, "r", encoding="utf-8")
lines = file.readlines()
file.close()


## Except Text
except_list = [
'Teardown',
'Built inbound',
'Built outbound',
'access-list'
]


## Main
cnt = 0

for line in lines:
  cnt = 0
  if cnt < 1:
    for find in except_list:
      p = re.findall(find, line, re.I)
      len_p = len(p)
      
      if len_p > 0:
        cnt = 1
        break
        
      else:
        continue
        
  if cnt < 1:
    w_txt = open(p_outfile, "a", encoding="utf-8")
    w_txt.writelines(line)
    w_txt.close()
    
    
print ("\n\n    :::: Success !! ::::\n")




