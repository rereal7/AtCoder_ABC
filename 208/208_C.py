n, k = map(int, input().split())
a = list(map(int, input().split()))
b = sorted(a)

x = k//n
y = k%n
t = b[y-1]

for i in range(n):
	if y != 0 and a[i] <= t:
		print(x+1)
	else:
		print(x)