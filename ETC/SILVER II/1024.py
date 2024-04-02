import sys
N, L = list(map(int, sys.stdin.readline().split(" ")))
isFound = False

for i in range(L-1, 100):
    x = ((2 * N - i * (i + 1)) / (2 * (i + 1))) 
    if x.is_integer() :
        intX = int(x)
        if(intX >= 0):
            for j in range(intX, intX + i+1):
                print(j, end=" ")
            isFound = True
            break

if not isFound:
    print(-1)
