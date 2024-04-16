ALen, BLen = map(int, input().split())

setA = set(map(int, input().split()))
setB = set(map(int, input().split()))

resultSet = setA ^ setB
print(len(resultSet))