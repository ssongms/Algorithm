N = int(input())
room = [list(input()) for _ in range(N)] # 방 구조 입력

widthResult = 0
heightResult = 0

if N == 1:
    print("0 0")
else:
    # 가로 체크
    for line in room:
        strLine = ''.join(line)
        XCount = strLine.count('X')
        if XCount > 0:
            layList = strLine.split('X')

            for laySpace in layList:
                if laySpace.count('..') > 0:
                    widthResult += 1
                    continue
        else:
            widthResult += 1
            continue
        
        

    # 세로 체크
    newRoom = [['.' for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            newRoom[i][j] = room[j][i]

    for line in newRoom:
        strLine = ''.join(line)
        XCount = strLine.count('X')
        if XCount > 0:
            layList = strLine.split('X')

            for laySpace in layList:
                if laySpace.count('..') > 0:
                    heightResult += 1
                    continue
        else:
            heightResult += 1
            continue
            
    print(widthResult, heightResult)