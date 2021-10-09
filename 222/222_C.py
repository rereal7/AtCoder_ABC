n,m = map(int, input().split())

# 2n人の選手の、それぞれの出し手
A = []
for i in range(2*n):
	A.append(input())

# print(A[0][0])

# 必要なのは
# 1.各ラウンドの対戦相手を決定すること
# 2.対戦相手との勝負の結果を記録するMap
# 3.対戦相手との勝負の結果を決定する条件分岐

result = {i:0 for i in range(2*n)}

for i in range(m):
	res = sorted(result.items(), key=lambda x:x[1], reverse=True)
	r_list = list(result.keys())
	for k in range(1, n+1):
		# 対戦相手を確定する(index調整のため-1)
		p1 = res[2*k-1][0]
		p2 = res[2*k-2][0]

		# 対戦を行う
		p1_GCP = A[p1][i]
		p2_GCP = A[p2][i]
		if p1_GCP == 'G':
			if p2_GCP == 'C':
				result[p1] += 1
			elif p2_GCP == 'P':
				result[p2] += 1
		elif p1_GCP == 'C':
			if p2_GCP == 'P':
				result[p1] += 1
			elif p2_GCP == 'G':
				result[p2] += 1
		elif p1_GCP == 'P':
			if p2_GCP == 'G':
				result[p1] += 1
			elif p2_GCP == 'C':
				result[p2] += 1


res = sorted(result.items(), key=lambda x:x[1], reverse=True)
for i in range(2*n):
	print(res[i][0]+1)

# result = sorted(result.items(), key=lambda x:x[1], reverse=True)
# r_list = list(result.keys())
# print(r_list)

# print(result)