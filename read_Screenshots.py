#-*-coding:utf-8-*-
import re
from os import walk
from PIL import Image
import pytesseract

path=r'C:\Users\User\Pictures\XiaoYaoPic\Screenshots'

for dirpath,dirnames,name in walk(path):
	n=name[-1]
path=path+"\\"+n
source = Image.open(path)
text  = pytesseract.image_to_string(source,lang='chi_sim')

f=open(r"D:\text.txt","w+")
f.write(text.encode('utf-8'))
f.close()
f=open(r"D:\text.txt","r")
for line in f.readlines():
	print line
f.close()
print "Done"

baidu=r"https://www.baidu.com/baidu?&ie=utf-8&word="
