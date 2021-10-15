# あいこになる条件は
# 1.すべての手が同じとき
# 2.すべての手が異なるとき

x,y = map(int,input().split())
if x == y:
	print(x)
else:
	print(3-(x+y))