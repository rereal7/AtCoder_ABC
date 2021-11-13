n = int(input())
S = list(map(int, input().split()))

ans = n
for s in S:
	flag = False
	for a in range(1,1001):
		for b in range(1, 1001):
			area = 4*a*b + 3*a + 3*b
			if s == area:
				flag = True
	if flag:
		ans -= 1

print(ans)