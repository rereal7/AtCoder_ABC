s = input()
n = len(s)
t = 'chokudai'
mod = 1000000007

# dpの箱の準備
dp = [[0 for i in range(9)] for j in range(n+1)]
# print(dp)

# 初期化(番兵の値を適切なものにする)
for i in range(n+1):
	dp[i][0] = 1

# 漸化式をコードに変換していく
for i in range(n):
	for j in range(8):
		if s[i] != t[j]:
			dp[i+1][j+1] = dp[i][j+1]
		else:
			dp[i+1][j+1] = (dp[i][j+1] + dp[i][j]) % mod
print(dp[n][8])

# 別解
# 配るDPとして求める
s = input()
n = len(s)
t = 'chokudai'
mod = 1000000007

# dpの箱の準備
dp = [[0 for i in range(9)] for j in range(n+1)]
# print(dp)

# 初期化(番兵の値を適切なものにする)
dp[0][0] = 1

# 漸化式をコードに変換していく
for i in range(n):
	for j in range(9):
		# 右隣に配る
		dp[i+1][j] = (dp[i+1][j] + dp[i][j]) % mod
		# 右下に配る
		if j < 8 and s[i] == t[j]:
			dp[i+1][j+1] = (dp[i+1][j+1] +dp[i][j]) % mod
print(dp[n][8])

# 別解
# 1次元のDPとして求める
s = input()
n = len(s)
t = 'chokudai'
mod = 1000000007
dp = [0 for i in range(9)]
dp[0] = 1

for i in range(n):
	for j in range(8):
		# 右下に配る
		if s[i] == t[j]:
			dp[j+1] = (dp[j+1] +dp[j]) % mod
print(dp[8])