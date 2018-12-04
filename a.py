#统计文件行数
count,blanks=0,0
with open ("a.txt") as fp:
	while True:
		line=fp.readline()
		if not line:
			break
		if(len(line)-1)==0:#统计空白行
			blanks+1
		count+=1
print(count,blanks)