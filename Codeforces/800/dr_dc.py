t = int (input())

for i in range(t):
    n = int(input())
    s = input().strip()

    cnt = s.count('1')
    ans = 0

    for c in s:
        if c == '1':
            ans+=cnt-1
        else:
            ans+=cnt+1
    
    print(ans)
