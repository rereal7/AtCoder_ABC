# 参考[#25966088](https://atcoder.jp/contests/abc219/submissions/25966088)

X = input()
N = int(input())
S = []
for i in range(N):
	S.append(input())

# Xの英小文字の辞書を作成する(参考:https://note.nkmk.me/python-dict-create/)
# book = dict(zip(X, range(26)))
# print(book)
# {'b': 0, 'a': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'z': 24, 'y': 25}

# str.maketrans() でtableを作成し
# s.transrate(table) で文字の変換をしているので、対になっているみたい

# lambda関数(参考:https://note.nkmk.me/python-lambda-usage/)

table = str.maketrans(dict(zip(X, range(26))))
S.sort(key=lambda s: s.translate(table))
 
for ans in S:
	print(ans)