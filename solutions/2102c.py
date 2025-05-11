t = int(input())

# Construct entire solution and only print desired nxn grid
start = 249
order = [(start,start)]
for n in range(2,501):
    offset = start - (n-1) // 2
    # Extend solution from below
    if n % 2 == 0:
        for i in range(n-1):
            order.append((offset+i, offset+n-1))
        for j in range(n-1):
            order.append((offset+n-1, offset+j))
        order.append((offset+n-1, offset+n-1))
    else:
        # Extend solution from above
        for i in range(1, n):
            order.append((offset + i, offset))
        for j in range(1, n):
            order.append((offset, offset + j))
        order.append((offset, offset))

solution = [[0 for _ in range(500)] for _ in range(500)]
for card, ij in enumerate(order):
    i = ij[0]
    j = ij[1]
    try:
        solution[i][j] = card
    except IndexError:
        print(ij, card)

for _ in range(t):
    n = int(input())

    # Possible greedy solution?
    # n = 1
    # 0

    # Assume we have the best solution for n = i
    # For n = i+1,
    #   any subgrid not including entire i subgrid will have MEX = i
    #   The next two MEX values greater than i will come from:
    #       the entire i+1 x i+1 subgrid
    #       one of the two i+1 x i subgrids
    #           to maximise this subgrid, we put the smallest consecutive numbers to maximise MEX
    #   Also want to keep 0 card as centred as possible since then it will add more non zero MEX subgrids
    for i in range(n):
        offset = start-(n-1)//2
        print(" ".join(map(str, solution[offset + i][offset:(offset+n)])))