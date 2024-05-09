import sys
N = int(sys.stdin.readline())
stuInfo = [list(sys.stdin.readline().split()) for _ in range(N)]

stuInfo.sort(key = lambda x : (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for name in stuInfo:
    print(name[0])