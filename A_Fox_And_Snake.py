r, c = map(int, input().split())
f=True
for i in range(r):
    if(i%2==0):
        print("#"*c)
    else:
        if f:
            print("."*(c-1)+"#")
        else:
            print("#"+"."*(c-1))
        f= not f