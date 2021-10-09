n = input()
x = len(n)
if x == 1:
	print(f'000{n}')
elif x == 2:
	print(f'00{n}')
elif x == 3:
	print(f'0{n}')
else:
	print(n)