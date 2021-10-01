n, a, x, y = map(int, input().split())
ans = 0
for i in range(n):
	if i < a:
		ans += x
	else:
		ans += y
print(ans)