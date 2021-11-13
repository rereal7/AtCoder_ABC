# 解説確認後
n = int(input())
ans = 0
for a in range(1, n+1):
	if a*a*a > n:
		break
	for b in range(a, n+1):
		if a*b*b > n:
			break
		ans += n//a//b-b+1
print(ans)

# コンテスト中のコードを修正したもの
n = int(input())
ans = 0
for a in range(1, n+1):
	if a*a*a > n:
		break
	for b in range(a, n//a+1): # 切り捨てだと生じる誤差を考慮
		c = n//a//b
		if a*b*c > n or c < b:
			break
		# print(f'a:{a} b:{b} c:{c}')
		ans += c-b+1
print(ans)