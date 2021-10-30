n = int(input())
AB = [list(map(int,input().split())) for i in range(n-1)]

ans = {i+1:0 for i in range(n)}
for a,b in AB:
	if a in ans:
		ans[a] += 1
	if b in ans:
		ans[b] += 1

ans = list(ans.values())
if max(ans) == n-1:
	print('Yes')
else:
	print('No')