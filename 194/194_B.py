# 解説確認後
# N<=1000なので2重ループの全探索で間に合う

n = int(input())
AB = [list(map(int, input().split())) for _ in range(n)]
A = [AB[i][0] for i in range(n)]
B = [AB[i][1] for i in range(n)]

ans = 10**10
for i in range(n):
	for j in range(n):
		ans = min(ans, A[i] + B[j] if i == j else max(A[i], B[j]))

print(ans)