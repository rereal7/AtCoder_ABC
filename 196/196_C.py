# 解説確認後
n = int(input())
for i in range(1, 1000001):
	if int(str(i) * 2) > n:
		print(i - 1)
		exit()


# 二分探索
n = int(input())

left = 0 # 「1」が条件を満たすこともあるので、初期値は0
right = 1000000

while right - left > 1:
	mid = (right + left) // 2
	# print(f'left:{left} right:{right}')
	f = int(str(mid) * 2)
	if f <= n:
		left = mid
	else:
		right = mid

ans = left
print(ans)