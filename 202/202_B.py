S = input()
ans = ''
for s in reversed(S):
	if s == '0':
		ans += '0'
	elif s == '1':
		ans += '1'
	elif s == '6':
		ans += '9'
	elif s == '8':
		ans += '8'
	elif s == '9':
		ans += '6'
print(ans)

# 別解(置換を使えばもっと高速にできる)
s = input()
s = s.replace('6', 'a')
s = s.replace('9', '6')
s = s.replace('a', '9')
ans = s[::-1]
print(ans)