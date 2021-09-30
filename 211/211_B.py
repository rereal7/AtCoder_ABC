# 共通部分
H = ['H', '2B', '3B', 'HR']
S = []
for i in range(4):
	S.append(input())

# 解答1 1つずつ一致するか確認する
ans = 'Yes'
for i in H:
	if i not in S:
		ans = 'No'
		break
print(ans)

# 解答2 集合としてみて、ソートしたものが一致するか確認する
H.sort()
S.sort()
if H == S:
	print('Yes')
else:
	print('No')

# 解答3 重複しているかどうかを確認する(本問では、重複は認められない)
if len(set(S)) == 4:
	print('Yes')
else:
	print('No')