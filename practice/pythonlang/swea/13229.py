T = int(input())
day_arr = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]

for i in range(1, T+1):
    input_str = input()
    index = day_arr.index(input_str)
    if index == 6:
        print(f"#{i} {7}")
    else:
        print(f"#{i} {6 - index}")