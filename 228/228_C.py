n,k = map(int, input().split())
P = [list(map(int, input().split())) for _ in range(n)]
totalScore = [sum(P[i]) for i in range(n)]

# print(totalScore)