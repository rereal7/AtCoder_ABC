# TLEになる
# n = int(input())
# A = list(map(int, input().split()))

# ans = 0
# for i in range(n-1):
# 	for j in range(i+1, n):
# 		if abs(A[i]-A[j]) %200 == 0:
# 			ans += 1
# 		# print(f'{i} {j} {ans}')
# print(ans)

# 正解
n = int(input())
A = list(map(int, input().split()))
B = {i:0 for i in range(200)}
for i in range(n):
	if A[i]%200 not in B:
		B[A[i]%200] = 1
	else:
		B[A[i]%200] += 1
ans = 0
for i in range(200):
	ans += (B[i]*(B[i]-1))//2
print(ans)