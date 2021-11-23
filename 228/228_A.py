s,t,x = map(int, input().split())
if s < t:
	# print("Yes" if s <= x < t else "No")
	if s <= x < t:
		print('Yes')
	else:
		print('No')
else:
	# print("Yes" if x < t or s <= x else "No")
	if x < t or s <= x:
		print('Yes')
	else:
		print('No')