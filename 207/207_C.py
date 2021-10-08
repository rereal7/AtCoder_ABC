# 参照(https://atcoder.jp/contests/abc207/editorial/2152)

n = int(input())
l = [0]*n
r = [0]*n

# 各区間を閉区間に直す(場合分けのパターン数をへらすため)
for i in range(n):
	t,l[i],r[i] = map(int, input().split())
	if t == 2:
		r[i] -= 0.5
	elif t == 3:
		l[i] += 0.5
	elif t == 4:
		l[i] += 0.5
		r[i] -= 0.5

# 共通部分を持つかの判定
ans = 0
for i in range(n):
	for j in range(i+1, n):
		# ans += (max(l[i],l[j]) <= min(r[i],r[j]))
		if max(l[i],l[j]) <= min(r[i],r[j]):
			ans += 1

print(ans)