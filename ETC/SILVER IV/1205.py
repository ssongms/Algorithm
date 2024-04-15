# https://www.acmicpc.net/problem/1205

N, newScore, size = map(int, input().split())
if N > 0:
    queue = [-1] * size
    scores = list(map(int, input().split()))
    for i in range(len(scores)):
        queue[i] = scores[i]

    if queue[size-1] != -1 and queue[size-1] >= newScore:
        print(-1)

    else: # 새로운 점수 삽입 가능
        newQueue = []
        for i in range(size):
            if newScore < queue[0]:
                queue.pop(0)
            else:
                print(i+1)
                break
else:
    print(1)