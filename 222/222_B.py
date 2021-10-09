n,p = map(int, input().split())
A = map(int, input().split())

ans = 0
for i in A:
	if i < p:
		ans += 1
print(ans)