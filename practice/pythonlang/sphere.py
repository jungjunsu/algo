input_r = float(input("구의 반지름을 입력해주세요: "))
pi = 3.14159265

print(f"""
= 구의 부피는 {4/3 * pi * (input_r**3)}입니다.
= 구의 겉넓이는 {4 * pi * (input_r**2)}입니다.
""".strip())
