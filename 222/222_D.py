n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
mod = 998244353

C = [0 for i in range(n)]
c = 0
for i in range(n):
	# A[i]のほうが大きい場合は条件に反する
	if A[i] > B[i]:
		continue
	# Cが取りうる数字の範囲を決定する必要がある
	C[i] = B[i]-A[i]+1
	if i > 0 and B[i-1]>A[i]:
		c += B[i-1]-A[i]

ans = 1
for i in range(n):
	if C[i] != 0:
		ans *= C[i]
print((ans -c)%mod)