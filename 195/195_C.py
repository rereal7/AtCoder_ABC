# 解説確認後
n = int(input())

count = 0
i = 1
while True:
	notCount = int('999'*i)
	if n - notCount < 0:
		break
	else:
		count += n - notCount
		i += 1

print(count)