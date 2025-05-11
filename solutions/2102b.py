t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    # If (n - 1)//2 numbers have absolute value larger than a1 then solution exists
    count = 0
    for i in range(1, n):
        if abs(a[0]) < abs(a[i]):
            count += 1

    result = "NO"
    if count >= (n-1) // 2:
        result = "YES"
    print(result)