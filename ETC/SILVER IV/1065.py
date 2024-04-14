arr = [0] * 1001
N = int(input())
for i in range(1, 100):
    arr[i] = 1 # 1~99까지 마킹
for i in range(100, 1000): # 세자리수
    if int(str(i)[2])-int(str(i)[1]) == int(str(i)[1])-int(str(i)[0]):
        arr[i] = 1
rangeArr = arr[:N+1]
print(rangeArr.count(1))
