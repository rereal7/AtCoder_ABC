# 別解について考えたい
a,b,c,d = map(int,input().split())
e = c
a += b

flag = False
if b/c >= d:
	flag = True
else:
	i = 1
	while a/e > d:
		a += b
		e += c
		i += 1

if flag:
	print(-1)
else:
	print(i)