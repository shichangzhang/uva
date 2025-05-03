t=int(input())
for i in range(0, t):
    test = i+1
    n, k, p = [int(x) for x in input().split()]

    # Coach passes to K
    start = k-1

    # Make P passes
    end = (start + p) % n + 1

    result = end
    print(f"Case {test}: {end}")