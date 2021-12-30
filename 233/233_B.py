l,r = map(int, input().split())
s = input()
s1 = s[:l-1]
s2 = s[l-1:r]
s3 = s[r:]
print(s1+s2[::-1]+s3)