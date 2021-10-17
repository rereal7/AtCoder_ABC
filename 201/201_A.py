A = map(int,input().split())
B = sorted(A)

ans = 'Yes'
if B[1] - B[0] != B[2] - B[1]:
	ans = 'No'

print(ans)