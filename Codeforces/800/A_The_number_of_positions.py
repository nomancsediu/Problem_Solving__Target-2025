n,a,b=map(int,input().split())
hotepare=0
for i in range(1,n+1):
    samne=i-1
    pisone=n-i

    if samne>=a and pisone<=b:
        hotepare+=1


print(hotepare)
    