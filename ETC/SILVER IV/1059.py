# https://www.acmicpc.net/problem/1059

L = int(input())
coordinates = list(map(int, input().split()))
N = int(input())
coordinates.append(N)
coordinates.sort()

if coordinates.count(N) > 1:
    print(0)
else:
    if coordinates[0] == N: # 첫 원소로 들어왔다면
        start = 1
    else:
        start = coordinates[coordinates.index(N)-1]+1
    end = coordinates[coordinates.index(N)+1]-1

    result = 0
    for i in range(start, N+1, 1):
        result += end-N+1
    
    print(result-1)