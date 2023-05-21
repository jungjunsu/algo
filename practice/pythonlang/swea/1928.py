T = int(input())
encoding_str = ""
encoding_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K",
                 "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
                 "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g",
                 "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",
                 "s", "t", "u", "v", "w", "x", "y", "z", 0, 1, 2, 3, 4,
                 5, 6, 7, 8, 9, "+", "/"]
bin_str = ""
decoding_str = ""
count = 0

def f_ord(x):
    if x in "0123456789":
        x = int(x)
    return encoding_list.index(x)

for i in range(1, T+1):
    encoding_str = input()
    bin_str = ""
    decoding_str = ""
    count = 0
    if len((encoding_str)) % 4 != 0 or len((encoding_str)) > 100000:
        exit(1)
    for x in encoding_str:
        bin_str += "{:06b}".format(f_ord(x))
    for x in range(0, len(bin_str), 8):
        decoding_str += chr(int(bin_str[x:x+8], 2))
    print(f"#{i} {decoding_str}")