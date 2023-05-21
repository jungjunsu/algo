TC = int(input())

for i in range(1, TC+1):
    N, Pd, Pg = list(map(int, input().split()))
    ans = "Broken"
    if Pd != 0 and Pg == 0:
        ans = "Broken"
    elif Pd != 100 and Pg == 100:
        ans = "Broken"
    else:
        for d in range(1, N + 1):
            if (Pd * d / 100) % 1 == 0:
                ans = "Possible"
                break
    print(f"#{i} {ans}")