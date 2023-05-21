input_val = int(input())
output_val = ""

if input_val > 100000:
    exit(1)
for i in range(input_val):
    output_val += "#"
print(output_val)