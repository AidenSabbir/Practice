import sys
print = sys.stdout.write
input = sys.stdin.readline
n = int(input())
for i in range(n):
    draw = 0
    arr = list(map(int,input().split()))
    while arr[2] != 0:
        if (arr[0] == arr[1] == 0) and arr[2]%2!=0:
            draw = -1
            break
        if arr[1] != 0:
            arr[2] = arr[2] -1
            arr[1] = arr[1] -1
            draw += 1
            arr.sort()
        else:
            break
    print(str(draw)+'\n')    