# TLEで間に合わず
n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))
A.sort()
C.sort()

num = 0
ans = 0
count = 0
for i in range(n):
	# A[i]がダブったらショートカットする
	if A[i] == num:
		ans += count
		continue
	else:
		num = A[i]
		count = 0

	# A[i]と一致する値を検索、カウントする
	b = [j for j, x in enumerate(B) if x == A[i]]
	for i in b:
		count += C.count(i+1)
	ans += count

print(ans)

# 正解を考える(参考(https://blog.hamayanhamayan.com/entry/2021/05/22/225302))
n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))
D = [B[C[j] - 1] for j in range(n)]

count = [0]*(10**5+1)  # count内に、0~10**5のインデックスを考慮して、+1する必要がある
for d in D:
	count[d] += 1
# print(count)

ans = 0
for a in A:
	ans += count[a]
print(ans)