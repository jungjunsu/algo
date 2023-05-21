T = int(input())
temp_dict = {str(x): 0 for x in range(100 + 1)}
most_val = 0
temp_val = 0

for i in range(T):
    index = input()
    student_score = list(map(int, input().split()))
    temp_dict = {str(x): 0 for x in range(100 + 1)}
    most_val = 0
    temp_val = 0

    if len(student_score) != 1000:
        exit(1)
    for score in student_score:
        if score < 0 or score > 100:
            exit(1)
        temp_dict[str(score)] += 1
    for k in temp_dict:
        if temp_dict[k] >= most_val:
            most_val = temp_dict[k]
            temp_val = k
    print(f"#{index} {temp_val}")