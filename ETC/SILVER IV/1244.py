switchLen = int(input())
switches = list(map(int, input().split()))
stuNum = int(input()) # 학생 수

for i in range(stuNum):
    gender, N = map(int, input().split())
    if gender == 1: # 남자
        for j in range(N, switchLen+1, N):
            if switches[j-1] == 0:
                switches[j-1] = 1
            else:
                switches[j-1] = 0

    else: # 여자
        if N == 1 or N == switchLen: # 처음이나 마지막을 받았을 때 자기 자신만 바꿈
            if switches[N-1] == 0:
                switches[N-1] = 1
            else:
                switches[N-1] = 0
        else:
            if switches[N-1] == 0:
                switches[N-1] = 1
            else:
                switches[N-1] = 0 # 우선 자기 자신을 바꿈

            front = N-1
            rear = N-1 
            while front > 0 and rear < switchLen-1:
                front -= 1
                rear += 1
                if switches[front] == switches[rear]:
                    if switches[front] == 1:
                        switches[front] = 0
                        switches[rear] = 0
                    else:
                        switches[front] = 1
                        switches[rear] = 1
                else:
                    break


for idx, switch in enumerate(switches, 1):
    print(switch, end=" ")
    if(idx % 20 == 0):
        print()
