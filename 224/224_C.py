# pypyにしたら時間間に合った
n = int(input())
A = []
for i in range(n):
	A.append(list(map(int,input().split())))

ans = 0
for i in range(n-2):
	for j in range(i+1, n-1):
		for k in range(j+1, n):
			#  A[i][j] => i:何個目の点か j:0がx,1がy
			s = abs((A[i][0]-A[k][0])*(A[j][1]-A[k][1]) - (A[j][0]-A[k][0])*(A[i][1]-A[k][1]))/2
			if s > 0:
				ans += 1

print(ans)
