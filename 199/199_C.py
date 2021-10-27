# 参照(https://atcoder.jp/contests/abc199/editorial/1162)
# 参照(https://atcoder.jp/contests/abc199/submissions/26357568)
n = int(input())
S = list(input())
q = int(input())
flag = False

for t in range(q):
	t,a,b = map(int, input().split())
	
	if t == 2: # 文字列の前半と後半を入れ替える
		flag = not flag
	else: # Sのa文字目とb文字目を入れ替える
		a -= 1
		b -= 1
		if not flag: # 偽ならそのまま入れ替える
			S[a], S[b] = S[b], S[a]
		else: # 真なら文字列が前半後半で反転しているのを考慮して入れ替える
			if a >= n:
				a -= n
			else:
				a += n
 
			if b >= n:
				b -= n
			else:
				b += n
			
			S[a], S[b] = S[b], S[a]

if flag:
	print(''.join(S[n:]) + ''.join(S[:n]))
else:
	print(''.join(S))