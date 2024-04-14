import math

x1, y1, x2, y2, x3, y3 = map(int, input().split())
if x1 == x2 == x3 or y1 == y2 == y3:
    print(-1.0)
elif x2-x1 != 0 and x3-x1 != 0 and (y2-y1)/(x2-x1) == (y3-y1)/(x3-x1):
    print(-1.0)
else:
    # (x1,y1) - (x2, y2), (x3,y3)
    firstSquare = (math.sqrt(pow(x1-x2, 2)+pow(y1-y2, 2)) + math.sqrt(pow(x1-x3, 2)+pow(y1-y3, 2))) * 2

    # (x2, y2) - (x1, y1), (x3, y3)
    secondSquare = (math.sqrt(pow(x2-x1, 2)+pow(y2-y1, 2)) + math.sqrt(pow(x2-x3, 2)+pow(y2-y3, 2))) * 2

    # (x3, y3) - (x1, y1), (x2, y2)
    thirdSquare = (math.sqrt(pow(x3-x1, 2)+pow(y3-y1, 2)) + math.sqrt(pow(x3-x2, 2)+pow(y3-y2, 2))) * 2
    print(max(firstSquare, secondSquare, thirdSquare) - min(firstSquare, secondSquare, thirdSquare))