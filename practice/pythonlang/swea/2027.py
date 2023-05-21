ans_str = ""

for i in range(5):
    for j in range(5):
        if i == j:
            ans_str += "#"
        else:
            ans_str += "+"
    ans_str += "\n"
print(ans_str)