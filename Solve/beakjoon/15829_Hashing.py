# 15829 Hashing / 구현, 문자열, 해싱

def hashing(string, l):
    r = 31
    m = 1234567891
    hash_value = 0

    for i in range(l):
        a = ord(string[i]) - 96
        hash_value += a*r**i % m

    return hash_value % m

l = int(input())
string = input()
print(hashing(string, l))