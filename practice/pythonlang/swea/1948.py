T = int(input())
date_dict = {"1":31, "2":28, "3":31, "4":30, "5":31, "6":30, "7":31, "8":31, "9": 30,
             "10":31, "11":30, "12":31}
sum = 0

def check_exp(month_a, day_a, month_b, day_b):
    if month_b < month_a:
        return True
    if month_a == month_b and day_b < day_a:
        return True
    return False

for i in range(1, T+1):
    month_a, day_a, month_b, day_b = list(map(int, input().split()))
    sum = 0
    if check_exp(month_a, day_a, month_b, day_b):
        exit(1)
    if month_a < month_b:
        for j in range(1, month_b - month_a):
            sum += date_dict[str(month_a + j)]
        sum += day_b
        sum += date_dict[str(month_a)] - day_a + 1
    else:
        sum = day_b - day_a + 1
    print(f"#{i} {sum}")