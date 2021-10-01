p = int(input())
min = 10000000

coins = [1]
for i in range(1, 10):
	coins.append(coins[i-1]*(i+1))

sum = 0
for i in reversed(coins):
	if i > p:
		continue
	else:
		sum += p//i
		p = p%i
print(sum)