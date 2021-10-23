# 解けてないけど、しばらく手つけない
h,w,n = map(int,input().split())
dp = [['G' for i in range(w+2)]for j in range(h+2)]
G =[]
for i in range(n):
	a,b,c = map(int,input().split())
	G.append([a,b,c])
	dp[a][b] = c
print(dp)

for i in range(n):
	x = G[i][0]
	y = G[i][1]
	count = 0
	for j in range(1, n-1):
		p = dp[x][y]
		if dp[x][y-j] > p: # 上
			y -= j
			count += 1
		elif dp[x+j][y] > p: # 右
			x += j
			count += 1
		elif dp[x][y+j] > p: # 下
			y += j
			count += 1
		elif dp[x-j][y] > p: # 左
			x -= j
			count += 1
	print(count)