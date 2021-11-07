# DFSらしい?
# 参考(https://atcoder.jp/contests/abc226/submissions/27086834)

n = int(input())
A = [list(map(int, input().split())) for _ in range(n)]

needs = [False] * n
needs[n-1] = True
ans = 0
for i in range(n-1, -1, -1):
	a = A[i]
	t = a[0]
	k = a[1]
	na = a[2:]

	if needs[i]:
		ans += t
		for j in na:
			j -= 1
			needs[j] = True

# print(needs)
print(ans)