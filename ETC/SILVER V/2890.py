R, C = map(int, input().split())
satellite = []
for i in range(R):
    line = input()
    satellite.append(line)

checkNum = ['1','2','3','4','5','6','7','8','9'] #숫자가 있는지 검사하기 위한 리스트
distance = [0] * 9
for line in satellite:
    reverseLine = line[::-1] # 뒤에서부터 얼마나 떨어져 있는 곳에 숫자가 위치하는지 찾기 위해 reverse
    for num in checkNum:
        if reverseLine.find(num) != -1:
            distance[int(num)-1] = reverseLine.find(num)
            break # 시간 단축을 위해 찾으면 바로 break

sortedDistanceList = sorted(list(set(distance))) # 중복 제거 & 정렬
for i in range(len(sortedDistanceList)):
    for j in range(len(distance)):
        if distance[j] == sortedDistanceList[i]: 
            distance[j] = i+1

for i in range(9): # 출력
    print(distance[i])