t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    # Greedily remove ai + 1 from array
    # n = 1: 1 array
    # assuming we have best number of arrays for n
    # then solution for n+1 would either be same as n if a_n+1 == a_n
    #                       or 1 more than solution for n if a_n+1 > highest unremoved ai for solution n + 1

    result = 1
    highest_unremoved_ai = a[0]
    for ai in a:
        if ai == highest_unremoved_ai:
            continue
        elif ai > highest_unremoved_ai + 1:
            highest_unremoved_ai = ai
            result += 1
    
    print(result)