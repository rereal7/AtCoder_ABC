n = input()
N = len(n)
n = sorted(n)
rn = ''.join(reversed(n))

x = ''
y = ''
for i in range(N):
	if i == 0:
		x += rn[i]
		continue
	elif i == 1:
		y += rn[i]
		continue
	X = int(x)
	Y = int(y)
	if X > Y:
		y += rn[i]
	else:
		x += rn[i]


X = int(x)
Y = int(y)
print(X*Y)