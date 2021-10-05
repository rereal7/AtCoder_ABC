price = 206
n = float(input())*1.08
n = int(n)
if n < price:
	print('Yay!')
elif n == price:
	print('so-so')
else:
	print(':( ')