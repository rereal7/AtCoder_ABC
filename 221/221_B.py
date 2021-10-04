s = input()
t = input()

ans = 'No'
for i in range(len(s)-1):
	if s == t:
		ans = 'Yes'
		break
	s_1 = list(s)
	tmp = s_1[i]
	s_1[i] = s_1[i+1]
	s_1[i+1] = tmp 
	if ''.join(s_1) == t:
		ans = 'Yes'
		break

print(ans)