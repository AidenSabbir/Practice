
mod = 10**9 + 7
p = 31
def hash(s,p,mod):
    hash_val = 0
    power = 1
    for ch in s:
        num = ord(ch) - ord('a') + 1
        hash_val = (hash_val + num*power)%mod
        power = (power*p)%mod
    return hash_val

def compute_power(s,p,mod):
    n = len(s)
    power = [1] * n
    for i in range(1,n):
        power[i] = (power[i-1] *p)%mod
    return power
def prefix_hash(s,p,mod):
    n = len(s)
    power = 1
    prefix = [0]*n
    prefix[0] = ((ord(s[0])-ord('a'))+1)%mod
    for i in range(1,n):
        val = ord(s[i]) - ord('a') + 1
        power = (power * p) %mod
        prefix[i] =( prefix[i-1] + val*power)%mod
    return prefix

def sub_hash(prefix,l,r,power,mod):
    result = prefix[r]
    if l > 0:
        result = (result - prefix[l-1] + mod) % mod
    result = (result * pow(power[l], mod-2, mod)) % mod
    return result

def main():
    n = input('string: ')
    m = input('string to check: ')
    hash_m = hash(m,p,mod)
    pre = prefix_hash(n,p,mod)
    power = compute_power(n,p,mod)
    c = 0
    l,r = 0,len(m) - 1
    while r < len(n):
        if hash_m == sub_hash(pre,l,r,power,mod):
            c += 1
        l += 1
        r += 1
    print(str(c))
main()



#-----------------------------------------------------------
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

