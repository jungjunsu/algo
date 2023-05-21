TC = int(input())

def check_same(str1, str2):
    i = 0
    len_s1 = len(str1)
    len_s2 = len(str2)
    check_len = 2 * len_s1

    while i < check_len:
        if str1[i % len_s1] != str2[i % len_s2]:
            return "no"
        i += 1
    return "yes"

for i in range(1,TC+1):
    S, T = input().split()
    if len(S) >= len(T):
        print(f"#{i} {check_same(S, T)}")
    else:
        print(f"#{i} {check_same(T, S)}")