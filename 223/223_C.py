n = int(input())
AB = [list(map(int, input().split())) for i in range(n)]
T = [AB[i][0]/AB[i][1] for i in range(n)]
# print(AB) # [[1, 3], [2, 2], [3, 1]]
# print(T) # [0.3333333333333333, 1.0, 3.0] 時間
half = sum(T)/2
# print(half) # 2.1666666666666665

timer = 0
target = 0
sumLength = 0
for i in range(n):
	timer += T[i]
	if timer > half:
		timer -= T[i]
		target = i
		break
	sumLength += AB[i][0]
# print(timer) # 1.333333333333333
# print(target) # 2
# print(sumLength)# 3
lastLength = AB[target][1]*(half-timer)
# print(lastLength) # 0.2777777777777778

print(sumLength+lastLength)

# 綺麗にまとめたやつ
# n = int(input())
# AB = [list(map(int, input().split())) for i in range(n)]
# time = [AB[i][0]/AB[i][1] for i in range(n)]
# halfTime = sum(time)/2

# timer = 0
# target = 0
# sumLength = 0
# for i in range(n):
# 	timer += time[i]
# 	if timer > half:
# 		timer -= time[i]
# 		target = i
# 		break
# 	sumLength += AB[i][0]
# lastLength = AB[target][1]*(halfTime-timer)

# print(sumLength+lastLength)