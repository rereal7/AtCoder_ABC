n = int(input())
M = {}
B = []
for i in range(n):
	a,b = input().split()
	b = int(b)
	B.append(b)
	M[b] = a

B.sort(reverse=True)
print(M[B[1]])

# 別解(より簡潔)
n = int(input())
M = []
for i in range(n):
	a,b = input().split()
	b = int(b)
	M.append([b,a])
M.sort(reverse=True)
print(M[1][1])