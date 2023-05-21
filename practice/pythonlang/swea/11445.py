T = int(input())

def check_str(P, Q, len):
    for i in range(len):
        if P[i] != Q[i]:
            return False

    return True

for i in range(1, T+1):
    P = input().strip()
    Q = input().strip()

    if len(Q) - len(P) == 1 and check_str(P, Q, len(P)) and Q[-1] == "a":
        print(f"#{i} N")
    else:
        print(f"#{i} Y")