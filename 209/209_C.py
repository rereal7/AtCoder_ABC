# 参考(https://atcoder.jp/contests/abc209/editorial/2228)

n = int(input())
C = list(map(int, input().split()))
mod = 1000000007
C.sort()
ans = 1
for i in range(n):
	ans = ans * max(0, C[i] - i) % mod
print(ans)