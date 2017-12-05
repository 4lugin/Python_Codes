## Python 3.6

import re
import shutil
import os

## File Link
n=0
m=0
file_arp = "C:\\test_arp\\arp.log"
file_save = "C:\\test_arp\\acl_result%d.log" %n
file_origin = "C:\\test_arp\\acl.log"
file_result = "C:\\test_arp\\Result.log"

file = open(file_result, "w")
file.close()
os.unlink(file_result)


## Arp Total-Count
key = int(input(">> arp.log IP Total-Count?: "))


## First Loop
c_arp = open(file_arp, "r")
c_lines = c_arp.readlines()
c_lines = list(map(lambda s: s.strip(), c_lines))
c_arp.close()


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
	file_origin = "C:\\test_arp\\acl_result%d.log" %n
	file_save = "C:\\test_arp\\acl_result%d.log" %k

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


print ("\n\n   :::: Success !! ::::\n")
