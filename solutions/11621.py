m = int(input())

C23 = []

# 3 ** 19 < 2 ** 31 < 3 ** 20
for i in range(32):
    for j in range(20):
        C23.append(2**i * 3**j)

C23.sort()

def next23(m):
    start = 0
    end = len(C23) - 1
    n = C23[end]

    while start < end:
        middle = (start + end) // 2
        if C23[middle] >= m:
            n = C23[middle]
            end = middle
        else:
            start = middle + 1

    return n

while m != 0:
    print(next23(m))
    m = int(input())