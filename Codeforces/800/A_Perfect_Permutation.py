num = int(input())

if (num%2!=0):
    print(-1)
else:
    arr = [0]*num
    for i in range (0,num,2):
        arr[i]=i+2
        arr[i+1]=i+1

    for i in arr:
        print(i)