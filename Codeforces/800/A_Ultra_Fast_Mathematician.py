num1=(input())
num2=(input())
len = len(num1)

res =""

for i in range(len):
    if num1[i]==num2[i]:
        res+='0'
    else:
        res+='1'


print(res)



