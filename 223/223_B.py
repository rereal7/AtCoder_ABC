s = input()
S = ['' for i in range(len(s))]
for i in range(len(s)):
	x = s[0]
	y = s[1:]
	s = y+x
	S[i] = s
T = sorted(S)

print(T[0])
print(T[len(T)-1])

# 別解
s = input()
n = len(s)
V = []
for i in range(n):
	V.append(s[i:n]+s[0:i])
print(V)
print(min(V))
print(max(V))