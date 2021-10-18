# 解答例（https://atcoder.jp/contests/abc201/editorial/1825）
# 0000 から 9999 までの 10*4通りの暗証番号それぞれについて高橋くんの記憶に合致するかを判定し、合致するものの個数を数えることでこの問題を解くことができます。
S = input()
ans = 0
for i in range(10000):
	# 0 以上 9999 以下の整数に leading zero を付けたものを擬似的に表現
    flag = [False]*10
    now = i
    for j in range(4):
        flag[now%10] = True
        now //= 10

    flag2 = True
    for j in range(10):
		# 0~9までの数字が一致するかチェック
        if S[j] == 'o' and not flag[j]:
            flag2 = False
		# 0~9までの数字が不正に含まれてないかチェック
        if S[j] == 'x' and flag[j]:
            flag2 = False
    ans += flag2
print(ans)