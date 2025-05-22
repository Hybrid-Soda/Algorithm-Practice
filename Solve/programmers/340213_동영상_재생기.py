# 340213 [PCCP 기출문제] 1번 - 동영상 재생기 / 구현, 시뮬레이션, 문자열 처리

def to_seconds(time):
    m, s = map(int, time.split(':'))
    return m * 60 + s


def to_mmss(time):
    m, s = divmod(time, 60)
    return f"{m:02d}:{s:02d}"


def solution(video_len, pos, op_start, op_end, commands):
    tot = to_seconds(video_len)
    now = to_seconds(pos)
    op_s = to_seconds(op_start)
    op_e = to_seconds(op_end)

    for cmd in commands:
        if op_s <= now <= op_e:
            now = op_e
        
        if cmd == 'prev':
            now = max(0, now-10)
        elif cmd == 'next':
            now = min(tot, now+10)
    
    if op_s <= now <= op_e:
        now = op_e

    return to_mmss(now)


res1 = solution("34:33", "13:00", "00:55", "02:55", ["next", "prev"])
print(res1)
res2 = solution("10:55", "00:05", "00:15", "06:55", ["prev", "next", "next"])
print(res2)
res3 = solution("07:22", "04:05", "00:15", "04:07", ["next"])
print(res3)