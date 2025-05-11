t = int(input())

for _ in range(t):
    n, m, p, q = map(int, input().split())
    # array size n
    # sum is m
    # sum of p consecutive numbers is q

    result = "YES"
    # if n % p == 0, m must equal (n // p) * q
    if n % p == 0 and m != (n / p) * q:
        result = "NO"

    print(result)