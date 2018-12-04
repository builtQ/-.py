#统计文件行数
from chardet import detect（charde是导入的包：CMD中导入pip install charde）
count,blanks=0,0
with open("a.txt",'rb') as fp:
	detect(fp.read())


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
