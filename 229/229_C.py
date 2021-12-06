n,w = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(n)]
AB.sort(reverse=True)

#############
# リファクタリング後
ans = 0
for i in range(n):
	ans += AB[i][0] * min(w, AB[i][1])
	w -= min(w, AB[i][1])

print(ans)

# ans = 0
# count = 0
# for i in range(n):
# 	nice = AB[i][0]
# 	g = AB[i][1]

# 	if count >= w:
# 		break

# 	if w - count >= g:
# 		ans += nice * g
# 		count += g
# 	else:
# 		ans += nice * (w - count)
# 		count += (w - count)

	# print(f'ans{ans} count{count}')

# print(ans)