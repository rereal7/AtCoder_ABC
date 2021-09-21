alp = 'abcdefghijklmnopqrstuvwxyz'
P = list(map(int, input().split()))
ans = ''
for i in range(len(P)):
	ans += alp[P[i]-1]
print(ans)