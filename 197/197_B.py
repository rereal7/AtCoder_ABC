h,w,y,x = map(int, input().split())
x -= 1
y -= 1
S = [list(input()) for _ in range(h)]

# 左下右上の順に探索
ans = 1 # 始点を含めるので初期値は1
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
for i in range(0, 4):
	X = x
	Y = y
	while True:
		X += dx[i]
		Y += dy[i]
		# print(f'{i}:{X}:{Y}')

		# 外に出たら終了
		if X < 0 or w <= X or Y < 0 or h <= Y:
			# print(f'{i}:{ans}')
			break
		# 行き止まりなら終了
		if S[Y][X] == '#':
			# print(f'{i}:{ans}')
			break

		ans += 1
print(ans)