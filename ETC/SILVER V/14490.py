import math
N,M = map(int, input().split(":"))
gcd = math.gcd(N,M)
print(N//gcd, ":", M//gcd, sep="")

