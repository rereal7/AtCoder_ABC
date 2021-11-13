n,k,a = map(int, input().split())

N = [i+1 for i in range(n)]
print(N[(k+a-2)%n])