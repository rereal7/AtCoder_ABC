n = int(input())
s = input()
for i in range(n):
	if i%2 == 0 and s[i] == '1':
		print('Takahashi')
		break
	elif i%2 == 1 and s[i] == '1':
		print('Aoki')
		break