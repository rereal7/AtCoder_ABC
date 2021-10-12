A = list(input().split())
A.sort()
if A[0] == A[1]:
	print(A[2])
elif A[1] == A[2]:
	print(A[0])
else:
	print(0)

# 別解
a,b,c = input().split()
if a == b:
	print(c)
elif b == c:
	print(a)
elif c == a:
	print(b)
else:
	print(0)