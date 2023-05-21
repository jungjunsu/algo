T = int(input())

for i in range(1, T+1):
    N, M = list(map(int, input().split()))
    nm_arr = [["0" for col in range(M)] for row in range(N)]
    case1 = -1
    case2 = -1
    flags = 0
    for row in range(N):
        nm_arr[row] = list(input())
    for row in range(N):
        for col in range(M):
            if nm_arr[row][col] != "?":
                if nm_arr[row][col] == "#":
                    case1 = (row + col) % 2
                else:
                    case2 = (row + col) % 2
    for row in range(N):
        for col in range(M):
            if nm_arr[row][col] != "?":
                if nm_arr[row][col] == "#":
                    if case1 != -1 and (row + col) % 2 != case1:
                        flags = 1
                else:
                    if case2 != -1 and (row + col) % 2 != case2:
                        flags = 1
    if case1 > -1 and case2 > -1 and case1 == case2:
        flags = 1
    if flags:
        print(f"#{i} impossible")
    else:
        print(f"#{i} possible")