testcase_num = int(input())
ans_arr = []
temp_arr = []

for i in range(testcase_num):
    sum = 0
    round = 0
    temp_arr = input().split()
    for j in temp_arr:
        if not (j.isdigit()) or int(j) < 0 or int(j) > 10000:
            exit(1)
        else:
            sum += int(j)
    if (sum / 10) >= (sum // 10 + 0.5):
        round = 1
    ans_arr.append(sum // 10 + round)

for i in range(testcase_num):
    print(f"#{i} {ans_arr[i]}")