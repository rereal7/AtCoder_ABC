a, b, c = map(int, input().split())
calc = c
ans = 0
while calc <= b:
	if calc >= a:
		ans = calc
		break
	else:
		calc += c


if ans == 0:
	print(-1)
else:
	print(ans)