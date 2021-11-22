n = int(input())
A = list(map(int, input().split()))

# それぞれの要素数を保持
dict = {}
for i in range(n):
	if A[i] not in dict:
		dict[A[i]] = 1
	else:
		dict[A[i]] += 1

# 要素を一意に定める
setA = list(set(A))
n = len(setA)

ans = 0
for i in range(n):
	for j in range(i+1, n):
		ans += (setA[i] - setA[j])**2 * dict[setA[i]] * dict[setA[j]]

print(ans)