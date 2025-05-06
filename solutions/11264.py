t = int(input())

for _ in range(t):
    n = int(input())
    c = list(map(int, input().split()))
    
    # Ci is Coin i
    # Counti is best count for solution containing Ci
    # Xi is the smallest amount withdrawn to achieve best solution containing Ci when only considering coins smaller than Ci (Ci <= Xi < 2Ci)
    #
    # For i = 1, X1 = 1, C1 = 1, Count1 = 1
    # Let's suppose I have the best solution including Ci represented by Counti and Xi
    # Let's construct a solution containing Ci+1:
    #   if Ci+1 > Xi, adding in Ci will achieve the best solution for Ci+1, Counti+1 = Counti + 1 and Xi+1 = Xi + Ci+1
    #   if Ci+1 <= Xi, removing Ci and adding Ci+1 will achieve the best solution for Ci+1, Counti+1 = Counti and Xi+1 = Xi - Ci + Ci+1
    #       Suppose Counti+1 > Counti
    #           then Xi = Xi+1 - Ci+1, but Ci+1 <= Xi, so Ci+1 <= Xi+1 - Ci+1
    #           which implies 2Ci+1 <= Xi+1, but this means Ci can be withdrawn twice from Xi+1
    #               meaning Xi+1 is not the smallest solution so by contradiction, Counti+1 <= Counti
    count = 1
    X = 1
    for i in range(1, n):
        if c[i] > X:
            count += 1
            X += c[i]
        else:
            X += -c[i-1] + c[i]

    result = count
    print(result)