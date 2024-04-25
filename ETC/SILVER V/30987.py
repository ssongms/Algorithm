x1, x2 = map(int, input().split())
a,b,c,d,e = map(int, input().split())

result = (a // 3) * (pow(x2, 3)-pow(x1, 3)) + ((b-d) // 2) * (pow(x2, 2)-pow(x1, 2)) + (c-e) * (x2-x1)
# 적분

print(result)