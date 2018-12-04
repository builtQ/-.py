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
#判断文件路径是否正确。isfile是原生字符串（r）
print(isfile(r"C:\a.txt"))
