W, H, X, Y, P = map(int, input().split())
result = 0
for i in range(P):
    peopleX, peopleY = map(int, input().split())

    # 왼쪽 원 방정식 안에 있는지 체크
    # (x-a)^2 + (y-b)^2 = r^2 => 원의 중심은 (a,b)
    if pow(peopleX-X, 2) + pow(peopleY-(Y+H//2), 2) <= pow(H//2, 2):
        result += 1

    # 내부 사각형 안에 있는지 체크
    elif X <= peopleX <= X+W and Y <= peopleY <= Y+H:
        result += 1

    # 오른쪽 원 방정식 안에 있는지 체크
    elif pow(peopleX-(X+W), 2) + pow(peopleY-(Y+H//2), 2) <= pow(H//2, 2):
        result += 1
    
print(result)