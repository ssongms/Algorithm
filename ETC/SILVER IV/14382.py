T = int(input())
result = []

for _ in range(T):
    N = int(input())
    if N == 0:
        result.append('INSOMNIA')
    else:
        originN = N
        numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        
        while len(numbers) != 0:
            strN = str(N)
            for i in range(len(strN)):
                if int(strN[i]) in numbers:
                    numbers.remove(int(strN[i]))
            N += originN

        result.append(N-originN)

for i in range(len(result)):
    print("Case #" + str(i+1) + ": " + str(result[i]))
