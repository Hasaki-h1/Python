#!/usr/bin/python
import os,sys,time 

def auto_attack():
	f = open("list.txt","r")
	for line in f.readlines():
		b = os.popen(line,'r',1)
		print(b.read())
i=1
while True:
    print("#############$$$$$$$---------The "+ str(i) +"th " + "attack---------$$$$$$$#############")
    auto_attack()
    time.sleep(3)
    i=i+1