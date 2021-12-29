x,y = map(int, input().split())
num = y - x

if num <= 0:
	print(0)
else:
	ans = 0
	while num > 0:
		num -= 10
		ans += 1
	print(ans)