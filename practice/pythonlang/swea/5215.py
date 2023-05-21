T = int(input())

def cal_recursion(next):
    global N
    global cal_max
    global N_list
    global ans_list
    global cal_list
    global depth_v
    global sum_v

    depth_v += 1

    if depth_v == N:
        ans_list.append(sum_v)
        return -1

    for i in range(next, N):
        if sum(cal_list) + N_list[i][1] <= cal_max:
            cal_list.append(N_list[i][1])
            sum_v += N_list[i][0]
            cal_recursion(i+1)
            depth_v -= 1
            sum_v -= N_list[i][0]
            cal_list.pop()
    if len(cal_list):
        ans_list.append(sum_v)
    return 0

for tc in range(1, T+1):
    N, cal_max = list(map(int, input().split()))
    N_list = [[0 for _ in range(2)] for _ in range(N)]
    cal_list = []
    ans_list = []
    sum_v = 0
    depth_v = -1
    for i in range(N):
        N_list[i] = list(map(int, input().split()))
    cal_recursion(0)
    if len(ans_list):
        print(f"#{tc} {max(ans_list)}")
    else:
        print(f"#{tc} 0")