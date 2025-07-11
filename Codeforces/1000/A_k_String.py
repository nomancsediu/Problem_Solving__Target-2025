from collections import Counter
k = int(input())
s = input()

map=Counter(s)

hobe=True
for c in map.values():
    if c%k!=0:
        hobe=False
        break
if not hobe:
    print('-1')
else:
    str=""
    for ch in map:
        str+=ch*(map[ch]//k)
    ans=str*k
    print(ans)


