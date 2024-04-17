def move(len, board):
    cycle = 0
    resultStr = []
    lenCount = 0
    while True:
        cycle += 1
        x = 0
        y = 0
        # 오른쪽으로 쭉 이동
        while board[cycle+x][cycle+y] != int(1e9):
            resultStr.append(board[cycle+x][cycle+y])
            board[cycle+x][cycle+y] = int(1e9)
            y+=1
            lenCount+=1
        if lenCount == len:
            break
        y-=1 # y를 하나 감소
        x+=1 # x를 하나 증가

        # 아래로 쭉 이동
        while board[cycle+x][cycle+y] != int(1e9):
            resultStr.append(board[cycle+x][cycle+y])
            board[cycle+x][cycle+y] = int(1e9)
            x+=1
            lenCount+=1
        if lenCount == len:
            break
        x-=1
        y-=1 

        # 왼쪽으로 쭉 이동
        while board[cycle+x][cycle+y] != int(1e9):
            resultStr.append(board[cycle+x][cycle+y])
            board[cycle+x][cycle+y] = int(1e9)
            y-=1
            lenCount+=1
        if lenCount == len:
            break
        y+=1
        x-=1

        # 아래로 쭉 이동
        while board[cycle+x][cycle+y] != int(1e9):
            resultStr.append(board[cycle+x][cycle+y])
            board[cycle+x][cycle+y] = int(1e9)
            x-=1
            lenCount+=1
        if lenCount == len:
            break
    
    return "".join(resultStr)

def switch(key):
    text = { 0:" ", 1:"A", 2:"B", 3:"C", 4:"D", 5:"E", 6:"F", 7:"G", 8:"H", 9:"I", 10:"J", 11:"K", 12:"L", 13:"M",
          14:"N", 15:"O", 16:"P", 17:"Q", 18:"R", 19:"S", 20:"T", 21:"U", 22:"V", 23:"W", 24:"X", 25:"Y", 26:"Z",
    }.get(key)
    return text

def transform(str):
    decimalList = []
    for i in range(0, len(str)-(len(str)%5), 5):
        binaryNum = '0b' + str[i:i+5]
        decimalList.append(int(binaryNum, 2))
    
    result = ""
    for decimal in decimalList:
        result += switch(decimal)
    print(result.rstrip())

# main
T = int(input()) #테스트 케이스 수
for i in range(T):
    strR, strC, msg = map(str, input().split())
    R = int(strR)
    C = int(strC) # string -> int

    board = [[int(1e9) for _ in range(C+2)]for _ in range(R+2)] # 상하좌우로 1칸씩 추가된 배열 생성
    
    msgCount = 0
    for x in range(1, R+1):
        for y in range(1, C+1):
            board[x][y] = msg[msgCount] # 입력 문자열을 배열에 복사
            msgCount += 1
    
    snailStr = move(R*C, board)
    transform(snailStr)