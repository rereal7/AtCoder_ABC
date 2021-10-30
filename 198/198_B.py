n = input()

flag = False
for i in range(len(n)):
	if n == n[::-1]:
		flag = True
		break
	n = '0' + n

if flag:
	print('Yes')
else:
	print('No')

# 公式(https://atcoder.jp/contests/abc198/editorial/223)
S=input()
for i in range(10):
	T = "0"*i + S
	if T==T[::-1]:
		print("Yes")
		exit()
print("No")