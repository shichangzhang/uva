n, m = map(int, input().split())
mountain = []

def check_diagonal(row, col, l, u):
    # Find smallest value bigger than l
    start = 0
    end = min(n-row-1, m-col-1)

    found = False
    while start < end:
        middle = (start + end) // 2
        
        if mountain[row + middle][col + middle] < l:
            start = middle + 1
        else:
            found = True
            end = middle

    if found:
        upper_left = start
    else:
        # Not found
        print(row, col, l, u)
        return 0
        
    # Find biggest value smaller than u
    start = 0
    end = min(n-row-1, m-col-1)

    found = False
    while start < end:
        middle = (start + end + 1) // 2
        if mountain[row + middle][col + middle] > u:
            end = middle - 1
        else:
            found = True
            start = middle

    if found:
        bottom_right = start
    else:
        # Not found
        return 0
    
    if upper_left <= bottom_right:
        return bottom_right - upper_left + 1
    else:
        return 0

while not (n == 0 and m == 0):
    mountain = []
    for _ in range(n):
        mountain.append(list(map(int, input().split())))
    
    q = int(input())
    for _ in range(q):
        l, u = map(int, input().split())

        result = 0
        # Check along each diagonal for biggest square
        for r in range(n):
            result = max(check_diagonal(r, 0, l, u), result)

        for c in range(1, m):
            result = max(check_diagonal(0, c, l, u), result)

        print(result)
    print("-")
    n, m = map(int, input().split())