#统计文件行数
from chardet import detect（charde是导入的包：CMD中导入pip install charde）
count,blanks=0,0
with open("a.txt",'rb') as fp:
	#检测文件编码，编码信息保存到code中
	code=detect(fp.read())['encoding']
	print(code)
	#detect(fp.read())


count,blanks=0,0
with open ("a.txt") as fp:
	while True:
		line=fp.readline()
		if not line:
			break
		if(line.strip)()==0:
		#if(len(line)-1)==0:#统计空白行
			blanks+1
		#print(len(line.strip()))
		count+=1
print(count,blanks)
#判断文件路径是否正确（正确为TRUE）；isfile是原生字符串（r）
print(isfile(r"C:\a.txt"))

import os
from chardet import detect
#isfile()这个函数是看给的路径对不，如果对，就返回ture，不对就返回fase
#a = os.path.isfile(r"C:\Users\Administrator\Desktop\root\a.txt")
root_path = os.getcwd()
dir_count,file_count = 0,0
for root,dirs,files in os.walk(root_path):
#os.path.isfile()检查该文件是否存在
    if not os.path.isfile(root):
        dir_count += 1
    for f in files:
	#print(os.path.join(root,f))#(文件路径)
        if os.path.isfile(os.path.join(root,f)):
            file_count =+ 1
print(dir_count-1,"Folders文件夹")
print(file_count,"Files文件")


print(dir_count-1)


import os
from chardet import detect
#isfile()这个函数是看给的路径对不，如果对，就返回ture，不对就返回fase
#a = os.path.isfile(r"C:\Users\Administrator\Desktop\root\a.txt")
root_path = os.getcwd()
dir_count,file_count = 0,0
#如果将这个程序打包到一个文件中，就把print改为句柄值，将所有的“，”转变位“+”，将所有的int转换位str
# info = open('文件名','w')
for root,dirs,files in os.walk(root_path):
    if not os.path.isfile(root):
        dir_count += 1
    for f in files:
        file_path = os.path.join(root,f )
        if os.path.isfile(file_path):
            file_count += 1
    print("filename",os.path.splitext(f)[0])
    print("type",os.path.splitext(f)[-1])
    print("size:",os.path.getsize(file_path),"Bytes")()
    print("location:",root)
    #get_file_info(file_path)
    print("_"*60)
print(dir_count-1,"Folders")
print(file_count,"Files")
