# 4659 비밀번호 발음하기 / 구현, 문자열

def test(string: str):
    def is_vowel(char: str):
        return char in 'aeiou'

    flag = False

    for i, c in enumerate(string):
        # 1. 모음(a,e,i,o,u) 하나를 반드시 포함하여야 한다.
        if is_vowel(c):
            flag = True

        # 2. 같은 글자가 연속적으로 두번 오면 안되나, ee 와 oo는 허용한다.
        if i > 0 and c == string[i-1] and c not in 'eo':
            return False
        
        # 3. 모음이 3개 혹은 자음이 3개 연속으로 오면 안 된다.
        if i > 1 and (
            (is_vowel(c) and is_vowel(string[i-1]) and is_vowel(string[i-2])) or
            not (is_vowel(c) or is_vowel(string[i-1]) or is_vowel(string[i-2]))
            ) :
            return False
    
    if not flag:
        return False
    
    return True

def main():
    while True:
        string = input()

        if string == 'end':
            break
        
        if test(string):
            print(f"<{string}> is acceptable.")
        else:
            print(f"<{string}> is not acceptable.")

if __name__ == '__main__':
    main()
