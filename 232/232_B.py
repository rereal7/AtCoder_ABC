s = input()
t = input()

# アルファベットの数だけ全探索する
for i in range(26):
    flag = True
    for j in range(len(s)):
        if t[j] != chr(97 + (ord(s[j])+i)%26):
            flag = False
            break
    if flag:
        break

print('Yes' if flag else 'No')