# LTE(1≤Ai≤10**9)になり不正解
n = int(input())
A = list(map(int, input().split()))

# 全探索で一致しない場合を数え上げる
ans = 0
for j in A:
	for i in range(0, j):
		if A[i] != A[j]:
			ans += 1

print(ans)

# 再考
n = int(input())
A = list(map(int, input().split()))

ans = 0
C = {}
for i in range(n):
	a = A[i]
	if a not in C:
		C[a] = 1
	else:
		C[a] += 1
	ans += i+1-C[a]
	# print(ans)
print(ans)