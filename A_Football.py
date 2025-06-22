n = int(input())
s = {}

for i in range(n):
    t = input().strip()
    if t in s:
        s[t] += 1
    else:
        s[t] = 1


for t in s:
    if s[t] == max(s.values()):
        print(t)
        break
