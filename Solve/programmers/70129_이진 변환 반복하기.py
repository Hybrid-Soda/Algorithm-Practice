def solution(s):
    answer = [0, 0]
    
    while s != '1':
        ones = get_ones(answer, s)
        s = binary_change(len(ones))
        answer[0] += 1

    return answer

def get_ones(answer, s):
    cnt_zero = s.count('0')
    answer[1] += cnt_zero
    return '1' * (len(s) - cnt_zero)

def binary_change(len_ones):
    return bin(len_ones)[2:]