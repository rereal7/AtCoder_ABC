import math

n = int(input())
P = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for i in range(n):
    for j in range(i, n):
        # 座標の定義
        x1 = P[i][0]
        x2 = P[j][0]
        y1 = P[i][1]
        y2 = P[j][1]

        # ２点間の距離
        edge = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

        ans = max(ans, edge)

print(ans)