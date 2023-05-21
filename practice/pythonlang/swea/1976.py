T = int(input())

for i in range(1, T+1):
    hour_a, min_a, hour_b, min_b = list(map(int, input().split()))
    if hour_a < 1 or hour_b < 1 or hour_a > 12 or hour_b > 12:
        exit(1)
    if not 0 <= min_a <= 59 or not 0 <= min_b <= 59:
        exit(1)
    hour = (hour_a + hour_b + (min_a + min_b) // 60) % 12
    min = (min_a + min_b) % 60
    print(f"#{i} {hour + 12 * (1 * (hour == 0))} {min}")