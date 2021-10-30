n,m = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(n)]

# 各列の値が7の倍数かチェック
for i in range(n-1):
	for j in range(m):
		x = B[i][j]
		y = B[i+1][j]
		if (y-x)%7 != 0:
			print('No')
			exit()

# 各行の値が逆の可能性, 右の値が左の値＋１ではない可能性を潰す
for i in range(n):
	for j in range(m-1):
		x = B[i][j]
		y = B[i][j+1]
		if x%7 == 0 or (y - x) != 1:
			print('No')
			exit()

print('Yes')