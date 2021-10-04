N = list(map(int,input().split()))
N.sort(reverse=True)
sum = N[0]+N[1]

print(sum)

# 別解
abc = list(map(int,input().split()))
print(sum(abc)-min(abc))