import sys
print = sys.stdout.write
MOD = 10**9+7
BASE = 2
power = [1] *((2*10**5)+1)
for i in range(1,((2*10**5)+1)):
    power[i] = (power[i-1]*BASE)%MOD
for _ in range(int(input())):
    n = int(input())
    a = input()
    b = input()
    c = 0
    path = a+b[-1]
    for i in range(n-1):
        if a[i+1] > b[i]:
            path = a[:i+1] + b[i:]
            break
    pathHash = 0
    for i in range(n+1):
        pathHash += (int(path[i])*power[i])%MOD
    initialPath = a[0]+b
    initialHash = 0
    for i in range(n+1):
        initialHash += (int(initialPath[i])*power[i])%MOD
    if initialHash == pathHash:
        c += 1
    curHash = initialHash
    for i in range(n-1):
        curHash = curHash - ((int(b[i])*power[i+1])%MOD) + ((int(a[i+1])*power[i+1])%MOD)
        if curHash == pathHash:
            c += 1
    print(path + '\n')
    print(str(c)+ '\n') 

