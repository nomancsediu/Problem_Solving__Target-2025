import math
t = int (input())
for i in range(t):
    s=int(input())
    r=int(math.sqrt(s))

    if r*r==s:
        print(0,r)
    else:
        print(-1)

