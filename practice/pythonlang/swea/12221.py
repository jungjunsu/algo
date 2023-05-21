TC = int(input())

for i in range(1, TC+1):
    A, B = list(map(int, input().split()))
    if A >= 10 or B >= 10:
        ans = f"#{i} -1"
    else:
        ans = f"#{i} {A*B}"
    print(ans)