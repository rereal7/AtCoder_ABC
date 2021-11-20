a,b = map(int, input().split())
ICE = {'ice_cream':1, 'ice_milk':2, 'lactic_ice':3, 'ice':4}
milk = a+b

if milk>=15 and b>=8:
	print(ICE['ice_cream'])
elif milk>=10 and b>=3:
	print(ICE['ice_milk'])
elif milk>=3:
	print(ICE['lactic_ice'])
else:
	print(ICE['ice'])