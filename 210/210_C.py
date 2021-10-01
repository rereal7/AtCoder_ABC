n, k = map(int, input().split())
C = list(map(int, input().split()))

# これだと実行時間が足りない
# ans = 0
# for i in range(n-k+1):
# 	tmp = []
# 	for j in range(k):
# 		tmp.append(C[i+j])
# 	ans = max(ans, len(set(tmp)))
# 	if ans == k:
# 		break
# print(ans)

T = {}
for i in range(k):
	if C[i] not in T:
		T[C[i]] = 1
	else:
		T[C[i]] += 1

max = len(T)
for i in range(k, n):
	outC = C[i-k]
	inC = C[i]
	# 左端の数字を排除し、辞書から削除、もしくはカウントを減らす
	if outC in T:
		T[outC] -= 1
		if T[outC] <= 0:
			del T[outC]
	# 右端に数字を追加し、辞書に登録、もしくはカウントを増やす
	if inC not in T:
		T[inC] = 1
	else:
		T[inC] += 1
	# 最大値を更新する
	if len(T) > max:
		max = len(T)

print(max)