N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
a = sorted(A)
b = sorted(B)

ans = 10**9
x = 0
y = 0
while x < N and y < M:
	ans = min(ans, abs(a[x]-b[y]))

	if a[x] < b[y]:
		x += 1
	else:
		y += 1

print(ans)
