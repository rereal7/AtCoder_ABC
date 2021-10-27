n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

a = max(A)
b = min(B)
count = b - a +1
if count > 0:
	print(count)
else:
	print(0)
