h,w = map(int,input().split())
A = []
for i in range(h):
	A.append(list(map(int,input().split())))

flag = True
for i in range(h-1):
	for j in range(w-1):
		left = A[i][j] + A[i+1][j+1]
		right = A[i+1][j] + A[i][j+1]
		if left > right:
			flag = False

if flag:
	print('Yes')
else:
	print('No')