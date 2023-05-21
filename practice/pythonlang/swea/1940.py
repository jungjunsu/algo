T = int(input())
current_vel = 0
accelerate = 0
move_range = 0

for i in range(1, T+1):
    N = int(input())
    current_vel = 0
    accelerate = 0
    move_range = 0
    if N < 2 or N > 30:
        exit(1)
    for j in range(N):
        command = list(map(int, input().split()))
        if len(command) > 1:
            accelerate = command[1] * (1 * (command[0] < 2) + -1 * (command[0] > 1))
            if current_vel + accelerate >= 0:
                current_vel = current_vel + accelerate
        move_range += current_vel

    print(f"#{i} {move_range}")