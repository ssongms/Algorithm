startYear, startMonth, startDay = map(int, input().split()) # 시작 연도, 달, 날짜 입력
endYear, endMonth, endDay = map(int, input().split()) # 끝 연도, 달, 날짜 입력

def isLeapYear(year): # 해당 년도가 윤년인지 체크하는 함수
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    return False

maxDay = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if (endYear == startYear+1000 and endMonth >= startMonth and endDay >= startDay) or (endYear >= startYear+1001):
    print("gg")
else:
    accDay = 0
    while startYear != endYear or startMonth != endMonth:
        if startMonth == 2: # 2월이면 해당 년도가 윤년인지 검사
            if isLeapYear(startYear): accDay += 29
            else: accDay += maxDay[startMonth]
        else: accDay += maxDay[startMonth]
        
        startMonth += 1 # 한 달 증가
        if startMonth == 13: # 13월이 되면 1월로 바꿔주고 년도 1 증가
            startMonth = 1
            startYear += 1
    
    accDay = accDay + (endDay - startDay)
    print("D-" + str(accDay))