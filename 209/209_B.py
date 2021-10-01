n, x = map(int, input().split())
A = list(map(int, input().split()))

if sum(A) <= x+(n//2*1):
	print('Yes')
else:
	print('No')