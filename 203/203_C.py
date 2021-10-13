n,k = map(int,input().split())
A = []
for i in range(n):
	A.append(list(map(int,input().split())))

# print(A)

result = {}
for i in range(n):
	a = A[i][0]
	b = A[i][1]
	if a not in result:
		result[a] = b
	else:
		result[a] += b

# print(result)
res = sorted(result.items(), key=lambda x:x[0])
# print(res) #  [(2, 3), (5, 5)]
for i in range(len(res)):
	if res[i][0] > k:
		break
	else:
		k += res[i][1]
print(k)