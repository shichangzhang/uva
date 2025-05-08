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
    can_reach = 0
    max_reach = 0
    result = 0
    for right in range(g):
        # Consider each station
        station = stations[right]
        if station[0] > can_reach:
        # Update can reach and increment result
            if max_reach > can_reach:
                result += 1
                can_reach = max_reach
        
        # If left is within reach then update max reach
        if station[0] <= can_reach:
            max_reach = max(max_reach, station[1])
        # If max reach is >= L then break, found solution
        if max_reach >= l:
            break
        # If max reach < left then break, no solution
        if max_reach < station[0]:
            break
    
    # if max reach > can reach then increment result one last time
    if max_reach > can_reach:
        result += 1
        can_reach = max_reach

    if max_reach >= l:
        print(g-result)
    else:
        print(-1)

    l, g = map(int, input().split())