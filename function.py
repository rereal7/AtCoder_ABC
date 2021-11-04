# 2分探索法テンプレ
def binary_search(key:int, A:list):
	ng = -1 # 「index = 0」が条件を満たすこともあるので、初期値は -1
	ok = len(A) # 「index = a.size()-1」が条件を満たさないこともあるので、初期値は len(A)

	# ok と ng のどちらが大きいかわからないことを考慮
	while (abs(ok - ng) > 1):
		mid = (ok + ng) // 2

		# mid が条件を満たすかどうか
		flag = False
		if A[mid] >= key :
			flag = True

		if flag:
			ok = mid
		else:
			ng = mid

	return ok

A = [1, 14, 32, 51, 51, 51, 243, 419, 750, 910]
print(binary_search(51, A)) # 3