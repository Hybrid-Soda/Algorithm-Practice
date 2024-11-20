# 1283 단축키 지정 / 구현, 문자열

n = int(input())
shortcuts = set()

for _ in range(n):
    strings = input().split()
    
    for i, string in enumerate(strings):
        if string[0].upper() not in shortcuts:
            strings[i] = string.replace(string[0], f'[{string[0]}]', 1)
            shortcuts.add(string[0].upper())
            break
    else:
        for i, string in enumerate(strings):
            for s in string:
                if s.upper() not in shortcuts:
                    strings[i] = string.replace(s, f'[{s}]', 1)
                    shortcuts.add(s.upper())
                    break
            else:
                continue
            break
    
    print(' '.join(strings))