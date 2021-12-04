n = int(input())
if len(str(n)) == 1 :
	print(f'AGC00{n}')
elif n < 42:
	print(f'AGC0{n}')
elif n >= 42:
	print(f'AGC0{n+1}')