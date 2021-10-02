# 未完成のコード
s = input()
t = input()

ans = 'No'
for i in range(len(s)-1):
	s_1 = s
	tmp = s_1[i]
	s_1[i] = s_1[i+1]
	s_1[i+1] = tmp 
	if s_1 == t:
		ans = 'Yes'
		break

print(ans)