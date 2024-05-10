N = int(input())
if N == 4 or N == 7: # 3과 5의 조합으로 못만드는 경우는 4와 7뿐
    print(-1)
else:
    result = 0
    if N % 5 == 0: # N이 5의 배수이면 따질 필요 없이 결과는 N / 5
        result = N // 5
        print(result)
    else:
        while True:
            N -= 3 # N에서 3을 빼고
            result += 1 # 3-봉지 1개 추가
            if N % 5 == 0:
                result += N // 5
                break
        print(result)