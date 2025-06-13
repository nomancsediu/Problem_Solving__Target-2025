y = int(input())

for y in range(y+1,10000):
    s = str(y)
    ans = set(s)
    if len(ans)==4:
        print(y)
        break
