# 1264 모음의 개수 / 구현, 문자열

VOWELS = set("aeiouAEIOU")

while True:
    line = input()
    
    if line == "#":
        break
    
    vowel_count = sum(1 for char in line if char in VOWELS)
    print(vowel_count)
