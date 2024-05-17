# # 기타콘서트 - https://www.acmicpc.net/problem/1497

import sys
from itertools import combinations

guitarNum, songNum = map(int, sys.stdin.readline().split())

guitars = []
for i in range(guitarNum):
    guitarName, availPlay = map(str, sys.stdin.readline().rstrip().split())
    toBinary = 0
    for j in range(songNum):
        if availPlay[j] == 'Y':
            toBinary |= (1 << j)
    guitars.append(toBinary)

max_songs = 0
min_guitars = guitarNum + 1

# Check all possible combinations of guitars
for i in range(1, guitarNum + 1):
    for comb in combinations(guitars, i):
        temp = 0
        for guitar in comb:
            temp |= guitar
        count = bin(temp).count('1')
        if count > max_songs:
            max_songs = count
            min_guitars = i
        elif count == max_songs:
            min_guitars = min(min_guitars, i)

if max_songs == 0:
    print(-1)
else:
    print(min_guitars)
