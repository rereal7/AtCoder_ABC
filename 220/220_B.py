k = int(input())
a, b = input().split()
ans = 0
sum_a = 0
sum_b = 0
for i in range(len(a)):
	sum_a += int(a[i])*(k**(int(len(a) -i -1)))
for i in range(len(b)):
	sum_b += int(b[i])*(k**(int(len(b) -i -1)))
print(sum_a*sum_b)
