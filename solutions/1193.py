n, d = map(int, input().split())
test = 1

while not (n == 0 and d == 0):
    # list of tuples of left and right most possible x position of radar
    # to detect each island
    islands = []
    result = 0

    for i in range(0, n):
        x, y = map(int, input().split())

        a = y
        c = d
        if a > c:
            result = -1
        else:
            b = (c*c - a*a) ** 0.5
            islands.append((x-b, x+b))

    if result != -1:
        # sort islands by right most possible radar position
        islands.sort(key=lambda x: x[1])

        # greedily place radar at right most position
        right = islands[0][1]
        result += 1
        for island in islands:
            if island[0] > right:
                # deploy another radar
                right = island[1]
                result += 1

    print(f"Case {test}: {result}")
    
    # empty line between test cases
    input()

    test += 1
    # read next test case
    n, d = map(int, input().split())