testcase_num = int(input())
ans_arr = []
date = 0

for i in range(testcase_num):
    error = 0
    date = int(input())
    year = date // 10000
    month = (date % 10000) // 100
    day = (date % 10000) % 100
    if month <= 0 or month > 12:
        error = 1
    if month in [1, 3, 5, 7, 8, 10, 12]:
        if not 1 <= day <= 31:
            error = 1
    elif month in [4, 6, 9, 11]:
        if not 1 <= day <= 30:
            error = 1
    else:
        if not 1 <= day <= 28:
            error = 1
    if error:
        ans_arr.append("-1")
    else:
        ans_arr.append("{:04d}/{:02d}/{:02d}".format(year, month, day))
for i in range(testcase_num):
    print(f"#{i+1} {ans_arr[i]}")