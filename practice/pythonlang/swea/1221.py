TC = int(input())
num_list = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

for _ in range(TC):
    tc, tc_len = input().split()
    tc_len = int(tc_len)
    tc_list = list(input().split())
    ans_str = f"{tc}\n"
    for i in range(tc_len):
        tc_list[i] = num_list.index(tc_list[i])
    tc_list.sort()
    for j in range(tc_len):
        ans_str += f"{num_list[tc_list[j]]} "
    print(ans_str.rstrip())