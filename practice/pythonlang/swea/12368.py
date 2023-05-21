T = int(input())

for i in range(1, T+1):
    A, B = list(map(int, input().split()))
    print(f"#{i} {A+B - 24 * ((A+B)//24)}")