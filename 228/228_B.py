n,x = map(int,input().split())
x -= 1
A = list(map(int,input().split()))
A = [A[i] - 1 for i in range(n)]

dict = {x:True}
while True:
	if A[x] not in dict:
		dict[A[x]] = True
		x = A[x]
	else:
		break

print(dict)
print(len(dict))