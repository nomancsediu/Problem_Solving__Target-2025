# ans = input()

# ans = ans.replace('--','2')
# ans = ans.replace('-.','1')
# ans = ans.replace('.','0')

# print(ans)


s = input()
i = 0
ans =''

while i<len(s):
    if s[i]=='.':
        ans+='0'
        i+=1
    elif s[i]=='-' and i+1<len(s):
        if s[i+1]=='.':
            ans+='1'
        else:
            ans+='2'
        i+=2

print(ans)



