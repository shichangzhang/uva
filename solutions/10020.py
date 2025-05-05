tests = int(input())

for test in range(0, tests):
    # Empty line between test cases
    input()

    intervals = []

    m = int(input())

    l, r = map(int, input().split())
    while not (l == 0 and r == 0):
        intervals.append((l, r))

        # Read next line
        l, r = map(int, input().split())

    # Treat negative values as 0, sort by Li ascending and Ri descending
    intervals.sort(key=lambda x: (max(0, x[0]), -max(0, x[1])))

    # Greedily pick intervals
    solution = []

    # [0, max_r] segment covered by line segments in solution
    max_r = 0

    # Sliding window
    left = 0
    right = 0
    while left < len(intervals):
        # Find interval which reachs furthest Ri where Li is <= max_r
        best_index = None
        best_interval = None
        while right < len(intervals):
            candidate_interval = intervals[right]
            if candidate_interval[0] > max_r:
                break
            else:
                if candidate_interval[1] > max_r:
                    if best_interval is None or candidate_interval[1] > best_interval[1]:
                        best_index = right
                        best_interval = candidate_interval
            right += 1
        if best_interval == None:
            # No solution
            break
        if max_r >= m:
            # Found solution
            break
        
        solution.append(best_interval)
        max_r = best_interval[1]
        left = right + 1

    # Print empty line between test cases
    if test > 0:
        print()

    if max_r >= m:
        print(len(solution))
        for interval in solution:
            print(f"{interval[0]} {interval[1]}")
    else:
        # No solution covering [0, m]
        print(0)