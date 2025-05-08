l, g = map(int, input().split())

while not (l == 0 and g == 0):
    stations = []
    for _ in range(g):
        x, r = map(int, input().split())
        # Save station range
        stations.append((max(0, x-r), x+r))
    # Sort stations by left end and if equal, sort by right end descending
    stations.sort(key=lambda x: (x[0], -x[1]))

    # Greedily pick station which reaches the furthest
    # Sliding window
    left = 0
    right = 0
    max_r = 0
    result = 0
    while left < g:
        best = None
        while right < g:
            station = stations[right]
            if station[0] > max_r:
                break
            else:
                if station[1] > max_r:
                    if best == None or station[1] > best:
                        best = station[1]
            right += 1
        if best == None:
            # No solution
            break
        if max_r >= l:
            # Found solution
            break

        max_r = best
        result += 1
        left = right

    if max_r >= l:
        print(g-result)
    else:
        print(-1)

    l, g = map(int, input().split())