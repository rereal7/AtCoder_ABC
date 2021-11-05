# 解説確認後
# O(1)
import math

a,b,w = map(int, input().split())
w *= 1000
max = int(math.floor(w/a))
min = int(math.ceil(w/b))

if min > max:
	print('UNSATISFIABLE')
else:
	print(min, max)

# 全探索
a,b,w = map(int, input().split())
w *= 1000

minOrange = w
maxOrange = 0
for select in range(1, w+1):
	left = a*select
	right = b*select
	if left <= w and w <= right:
		minOrange = min(minOrange, select)
		maxOrange = max(maxOrange, select)
if maxOrange == 0: # 可能性としては存在するので minOrange == w だとエラーを弾けない
	print('UNSATISFIABLE')
else:
	print(minOrange, maxOrange)