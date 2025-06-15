n = int(input())
m = int(input())

next_prime = -1

for i in range(n + 1, 51):
    flag = True
    for j in range(2, i):
        if i % j == 0:
            flag = False
            break
    if flag:
        next_prime = i
        break

if next_prime == m:
    print("YES")
else:
    print("NO")
