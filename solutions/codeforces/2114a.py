t = int(input())

for _ in range(t):
    s = int(input())

    b = int(s ** 0.5)
    if b * b == s:
        print (0, b)
    else:
        print(-1)