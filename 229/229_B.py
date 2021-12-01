a,b = map(list, input().split())

A = list(map(int, a[::-1]))
B = list(map(int, b[::-1]))
n = min(len(A), len(B))

flag = False
for i in range(n):
	# print(A[i] + B[i])
	if A[i] + B[i] >= 10:
		flag = True
		break

if flag:
	print('Hard')
else:
	print('Easy')