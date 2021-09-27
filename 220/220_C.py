n = int(input())
A = list(map(int, input().split()))
x = int(input())
calc = sum(A) * (x//sum(A))
ans = x//sum(A) * len(A)
for i in range(n):
	ans +=1
	calc += A[i]
	if calc > x:
		break
print(ans)