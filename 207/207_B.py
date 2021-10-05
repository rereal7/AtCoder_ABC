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

# 別解
a,b,c,d = map(int, input().split())
ans = -1
diff = c*d-b
if diff > 0:
	ans = (a+diff-1)//diff
print(ans)