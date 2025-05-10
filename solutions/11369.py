t = int(input())

for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    p.sort(reverse=True)

    result = 0
    for i, pi in enumerate(p, start=1):
        if i % 3 == 0:
            result += pi
    print(result)
