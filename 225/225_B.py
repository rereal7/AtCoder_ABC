# 反省点
# 1. 辞書型、リスト型への理解が足りていなかった点
# 2. 木（データ構造）が未履修だった点
# 3. 問題文の理解に時間がかかり過ぎた点

n = int(input())
AB = [list(map(int,input().split())) for i in range(n-1)]

ans = {i+1:0 for i in range(n)}
for a,b in AB:
	if a in ans:
		ans[a] += 1
	if b in ans:
		ans[b] += 1

ans = list(ans.values())
if max(ans) == n-1:
	print('Yes')
else:
	print('No')

# 別解
n = int(input())
AB = [list(map(int,input().split())) for i in range(n-1)]

ans = [0]*n
for i in range(n-1):
	a = AB[i][0]
	b = AB[i][1]
	ans[a-1] += 1
	ans[b-1] += 1

# if ans.count(1) == n-1 and ans.count(n-1) == 1: # こっちでもいける
if max(ans) == n-1:
	print('Yes')
else:
	print('No')