# まだ解けてないけど、しばらく手つけない予定
n,m = map(int,input().split())
V = []
for i in range(m):
	V.append(list(map(int,input().split())))

num = [i+1 for i in range(n)]
for i in range(n):
	if V[i][0] > V[i][1]:
		tmp = num[V[i][0]-1]
		num[V[i][0]-1] = num[V[i][1]-1]
		num[V[i][1]-1] = tmp
print(' '.join(str(num)))