#!/usr/bin/env python
# -*- coding:UTF-8 -*-
#time:2020/09/09 周三 15:33:20.24
#author:White9527

from xpinyin import Pinyin
import pypinyin,os,re
from pypinyin import lazy_pinyin,load_phrases_dict

def shanghai(wordlists,char=""):			#获取默认拼音格式	
	p = Pinyin()
	pwd = os.getcwd() + "\\dic" 
	if(os.path.exists(pwd)==False):
		os.makedirs(pwd)
	else:
		with open("./dic/shanghai.txt","w",encoding="utf-8") as f:
			for word in wordlist:
				str0 = p.get_pinyin(word,char)
				f.write(str0)
				print("默认拼音转换--->>>"+str0)
def SH(wordlists,char=""):					#获取拼音首拼大写
	p = Pinyin()
	pwd = os.getcwd() + "\\dic" 
	if(os.path.exists(pwd)==False):
		os.makedirs(pwd)
	else:
		with open("./dic/SH.txt","w",encoding="utf-8") as f:
			for word in wordlist:
				str0 = p.get_initials(word,char)
				f.write(str0)
				print("拼音首拼大写--->>>"+str0)

def shangh(wordlists):					#首字拼音加末尾首拼小写
	pwd = os.getcwd() + "\\dic" 
	if(os.path.exists(pwd)==False):
		os.makedirs(pwd)
	else:
		with open("./dic/shangh.txt","w",encoding="utf-8") as f:
			
			for word in wordlist:
				str0 = lazy_pinyin(word) 
				print(str0) #默认拼音列表
				stt1 = ""
				stt2 = ""
				stt3 = ""
				for st in str0:
					stt1 = str0[0]
					if(str0.index(st)>0):
						st1 = re.findall(r"\w",st)
						#print(type(st1))
						try:
							stt2 = stt2 + st1[0]
						except Exception as e:
							pass
				stt3 = stt1 + stt2 
				print("stt3->"+stt3)
				f.write(stt3+"\n")
				print("首字拼音加末尾首拼小写--->>>"+stt3)
				


if __name__ == '__main__':
	with open("name.txt","r",encoding="utf-8") as f:
		lis = f.readlines()
		wordlist = lis
		#print(wordlist)
		shangh(wordlist)








