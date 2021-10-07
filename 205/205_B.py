n = int(input())
A = list(map(int, input().split()))
x = n*(n+1)/2
# set()は引数がmapでも使える
if sum(A) == x and len(set(A)) == n:
	print('Yes')
else:
	print('No')