n,k = map(int, input().split())
P = [list(map(int, input().split())) for _ in range(n)]
totalScore = [sum(P[i]) for i in range(n)]
sortedScore = sorted(totalScore, reverse=True)

# print(totalScore)
# print(sortedScore)

for i in range(n):
	p = totalScore[i]
	if p+300 >= sortedScore[k-1]:
		print('Yes')
	else:
		print('No')