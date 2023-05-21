TC = int(input())

for i in range(1, TC+1):
    p, q = list(map(float, input().split()))
    s1 = (1-p)*q
    s2 = p*(1-q)*q
    if s1 < s2:
        print(f"#{i} YES")
    else:
        print(f"#{i} NO")