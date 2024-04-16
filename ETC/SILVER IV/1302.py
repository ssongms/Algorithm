sale = int(input()) # 오늘 팔린 책의 수
bookDict = dict()

for i in range(sale):
    name = input() # 책의 이름

    # 딕셔너리에 name이 key인 요소가 없으면 새로 추가 (value는 1)
     # 있다면 해당 이름을 key로 가진 요소의 value를 1 증가
    if name in bookDict:
        bookDict[name] += 1
    else:
        bookDict[name] = 1
maxSale = [k for k, v in bookDict.items() if max(bookDict.values()) == v]
maxSale.sort()
print(maxSale[0])