T = int(input())

def sum_recursion(next):
    global N
    global K
    global N_list
    global count_list
    global count
    global depth_v

    depth_v += 1
    if depth_v == N:
        if sum(count_list) == K:
            count += 1
        return -1
    for i in range(next, N):
        count_list.append(N_list[i])
        sum_recursion(i+1)
        depth_v -= 1
        count_list.pop()

    if sum(count_list) == K:
        count += 1
    return 1

for tc in range(1, T+1):
    N, K = list(map(int, input().split()))
    N_list = list(map(int, input().split()))
    count_list = []
    count = 0
    depth_v = -1
    sum_recursion(0)
    print(f"#{tc} {count}")