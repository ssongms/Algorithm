key = input()
cyphertext = input()
rowSize = (len(cyphertext) // len(key)) + 1
colSize = len(key)
board = [['@' for _ in range(colSize)]for _ in range(rowSize)]
result = [['@' for _ in range(colSize)]for _ in range(rowSize - 1)]
sortedKey = sorted(list(key))
for i in range(colSize):
    board[0][i] = sortedKey[i]
idx = 0
for i in range(colSize):
    for j in range(1, rowSize):
        board[j][i] = cyphertext[idx]
        idx += 1
keyList = list(key)
for i, elem in enumerate(board[0]):
    idx = keyList.index(elem)
    for j in range(rowSize-1):
        result[j][idx] = board[j+1][i]
    keyList[idx] = '@'

res1 = [''.join(row) for row in result]
res2 = ''.join(res1)
print(res2)
