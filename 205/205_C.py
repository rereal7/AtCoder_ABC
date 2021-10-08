# LTE(1≤C≤10**9 Cは指数)になり不正解
a,b,c = map(int,input().split())
d = pow(a,c)
e = pow(b,c)
if d<e:
	print('<')
elif d>e:
	print('>')
else:
	print('=')

# 再考
a,b,c = map(int,input().split())
if c%2 == 0:
	a = abs(a)
	b = abs(b)
	if a == b:
		print('=')
	elif a > b:
		print('>')
	elif a < b:
		print('<')
else:
	if a > b:
		print('>')
	elif a < b:
		print('<')
	else:
		print('=')