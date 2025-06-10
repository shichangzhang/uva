t = int(input())

cache = {}

def gcd(a, b):
    if (a, b) in cache:
        return cache[(a, b)]

    if a > b:
        return gcd(b, a)
    if a == 0:
        return b
    
    result = gcd(b % a, a)
    cache[(a, b)] = result
    return result

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    target = a[0]
    for i in range(1, n):
        target = gcd(target, a[i])

    # Target can be created in one move
    # proof:
    #   assume no pair ai, aj can create target
    #   this means all gcd(ai, aj) > target
    #   but gcd(a0, ..., an-1) = target by definition
    #   dodgy but proof by contradiction

    moves = 0
    if target in a:
        for i in range(n):
            if a[i] != target:
                moves += 1
    else:
        while target not in a:
            found = False
            min_gcd = a[0]
            min_i = 0
            min_j = 1
            for i in range(n):
                for j in range(i+1, n):
                    gcd_ij = gcd(a[i], a[j])
                    if gcd_ij < min_gcd:
                        min_gcd = gcd_ij
                        min_i = i
                        min_j = j
                    if gcd_ij == target:
                        a[i] = target
                        moves += 1
                        found = True
                        break
            if not found:
                a[min_i] = min_gcd
                moves += 1
        for i in range(n):
            if a[i] != target:
                moves += 1
    print(moves)