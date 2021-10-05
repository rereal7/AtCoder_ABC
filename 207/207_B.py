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
	# なぜ下記のような式になっているのか
	# まず、切り捨てが必要なので分母を分子に足す
	# ただし、割り切れてしまう時を考慮して、-1しておく必要がある
	ans = (a+diff-1)//diff
print(ans)