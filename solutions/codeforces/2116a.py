t = int(input())

for _ in range(t):
    a, b, c, d = map(int, input().split())

    # Gellyfish - a, flower - b
    # Gellyfish knight - c, flower knight - d

    if a >= b:
        if c >= d:
            print("Gellyfish")
        else:
            if c >= b:
                print("Gellyfish")
            else:
                print("Flower")
    else:
        if d > c:
            print("Flower")
        else:
            if d > a:
                print("Flower")
            else:
                print("Gellyfish")