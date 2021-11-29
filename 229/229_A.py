a = input()
b = input()

# if (a[0] == '.' and b[1] == '.') or (a[1] == '.' and b[0] == '.'):
# 	print('No')
# else:
# 	print('Yes')

AB = list(a+b)
count = AB.count('#')

if count > 2:
	print('Yes')
else:
	if AB[0] == AB[2] or AB[0] == AB[1]:
		print('Yes')
	else:
		print('No')