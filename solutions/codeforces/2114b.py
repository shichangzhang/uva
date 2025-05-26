t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    s = input()

    # Let a = # of 0s and b = # of 1s
    # then if we want exactly k good pairs the rest must be bad pairs
    # So must have equal number of 0s and 1s after taking out k good pairs
    # We'll have a minimum of abs(a-b)/2 good pairs
    # To balance 0s and 1s, we can then have abs(a-b)/2 + 2 * m pairs

    a = s.count('0')
    b = n-a
    pairs = abs(a-b)//2
    if pairs > k:
        print('NO')
    else:
        if k % 2 == pairs % 2:
            print('YES')
        else:
            print('NO')