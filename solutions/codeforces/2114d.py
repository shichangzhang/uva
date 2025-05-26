t = int(input())

for _ in range(t):
    # find smallest and largest 2 rows and columns and use them to determine boundaries
    monsters = []

    min_row = None
    min_row_2 = None
    max_row = None
    max_row_2 = None
    min_col = None
    min_col_2 = None
    max_col = None
    max_col_2 = None

    n = int(input())

    for i in range(n):
        x, y = map(int, input().split())
        monsters.append((x, y))
        if min_row is None:
            min_row = x
            max_row = x
            min_col = y
            max_col = y
        else:
            if min_row_2 is None:
                min_row_2 = max(min_row, x)
                min_row = min(min_row, x)

                max_row_2 = min(max_row, x)
                max_row = max(max_row, x)

                min_col_2 = max(min_col, y)
                min_col = min(min_col, y)

                max_col_2 = min(max_col, y)
                max_col = max(max_col, y)
            else:
                if x <= min_row:
                    min_row_2 = min_row
                    min_row = x
                elif x <= min_row_2:
                    min_row_2 = x
                if x >= max_row:
                    max_row_2 = max_row
                    max_row = x
                elif x >= max_row_2:
                    max_row_2 = x
                if y <= min_col:
                    min_col_2 = min_col
                    min_col = y
                elif y <= min_col_2:
                    min_col_2 = y
                if y >= max_col:
                    max_col_2 = max_col
                    max_col = y
                elif y >= max_col_2:
                    max_col_2 = y

    # print(min_row, min_row_2, max_row_2, max_row, min_col, min_col_2, max_col_2, max_col)

    if n == 1:
        print(1)
    elif n == 2:
        print(2)
    else:
        # Try moving each monster
        a = max_row - min_row + 1
        b = max_col - min_col + 1
        result = a * b

        for x, y in monsters:
            a = max_row - min_row + 1
            b = max_col - min_col + 1

            if x == min_row:
                a = max_row - min_row_2 + 1
            elif x == max_row:
                a = max_row_2 - min_row + 1
            if y == min_col:
                b = max_col - min_col_2 + 1
            elif y == max_col:
                b = max_col_2 - min_col + 1

            coins = a * b
            if coins < n:
                # No space for all monsters, need to add row or column
                coins += min(a, b)

            result = min(result, coins)
            # print(x, y, result)
        print(result)