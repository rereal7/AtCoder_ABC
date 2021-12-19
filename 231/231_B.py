n = int(input())
S = [input() for _ in range(n)]

result = {}
for s in S:
	if s not in result:
		result[s] = 1
	else:
		result[s] += 1

print(max(result.items(), key=lambda x:x[1])[0])

############ メモ
#
# maxメソッドはkey内の最大値を返す。
# 単純にmax()を使うとvalueで計算していないので、バグが混じった。
# valueで計算する場合は、items()メソッドを使い、lambdaで条件指定するとよい。
############