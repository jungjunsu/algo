T = int(input())
temp_arr = []
sum_val = 0
avr_val = 0

for i in range(1,T+1):
    temp_arr = list(map(int, input().split()))
    for j in temp_arr:
        if j < 0 or j > 10000:
            exit(1)
    temp_arr.remove(max(temp_arr))
    temp_arr.remove(min(temp_arr))
    sum_val = sum(temp_arr)
    avr_val = sum_val // 8
    if sum_val % 8 >= 4:
        avr_val += 1
    print(f"#{i} {avr_val}")