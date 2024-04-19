import math
N = int(input())
sqrtN = math.ceil(math.sqrt(N)) # 제곱근의 올림

if N <= 4:
    print(4)
else:
    width = sqrtN-1
    height = 0
    while True:
        N -= sqrtN
        height += 1
        if N <= sqrtN: break 
    print((height+width)*2) # 사각형의 둘레