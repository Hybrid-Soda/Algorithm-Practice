# 2744 대소문자 바꾸기 / 구현, 문자열

for s in input():
    print(s.lower() if s.isupper() else s.upper(), end='')