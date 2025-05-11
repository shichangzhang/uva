t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    # Suppose you have the permutation 1 2 3 4 5
    # Swap at 1, 3 4 1 2 5
    # Swap at 2, 3 2 5 4 1
    # Swap at 1, 5 4 3 2 1
    # Swap at 2, 5 2 1 4 3
    # So we have a 3 cycle 1 3 5
    
    # For 1 3 5 7
    # 3 cycle swap at 1, 3 5 1 7
    # 3 cycle swap at 3, 3 1 7 5
    # 3 cycle swap at 3, 3 7 5 1
    # 3 cycle swap at 1, 7 5 3 1
    # 3 cycle swap at 1, 5 3 7 1
    # 3 cycle swap at 3, 5 7 1 3