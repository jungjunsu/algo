T = int(input())
ans_str = ""

for i in range(1, T+1):
    A, B, C, D = list(map(int, input().split()))
    time_sum = 0
    if A <= C and B <= D and B >= C:
        time_sum = B - C
    elif A >= C and B >= D and A <= D:
        time_sum = D - A
    elif A <= C and B >= D:
        time_sum = D - C
    elif A >= C and B <= D:
        time_sum = B - A
    ans_str += f"#{i} {time_sum}\n"
print(ans_str.rstrip())