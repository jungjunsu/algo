testcase_number = int(input())
temp_arr = [0] * 10
answer_arr = [0] * testcase_number
 
for i in range(testcase_number):
    temp_arr[0], temp_arr[1], temp_arr[2], temp_arr[3], temp_arr[4], temp_arr[5], temp_arr[6], temp_arr[7], temp_arr[8], temp_arr[9] = input().split()
 
    for j in range(10):
        if (int(temp_arr[j]) < 0 or int(temp_arr[j]) > 10000):
            exit()
        elif (int(temp_arr[j]) % 2):
            answer_arr[i] += int(temp_arr[j])
 
for k in range(testcase_number):
    print('#' + str(k + 1) + ' ' + str(answer_arr[k]))
