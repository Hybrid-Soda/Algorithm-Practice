# 22862 가장 긴 짝수 연속한 부분 수열 (large) / 두 포인터

# 처음에는 두 포인터 다 왼쪽 끝에서 시작
n, k = map(int, input().split())
s = list(map(int, input().split()))
ans = even_cnt = odd_cnt = 0
l = r = 0

while r < n:
    # if 홀수 카운트가 k보다 크면 l 포인터 한칸 이동
    if odd_cnt > k:
        # 홀수: 홀수 카운트 감소
        if s[l] % 2:
            odd_cnt -= 1
        # 짝수: 짝수 카운트 감소
        else:
            even_cnt -= 1
        l += 1
    # elif 홀수 카운트가 k보다 작거나 같으면 r 포인터 한 칸 이동
    else:
        # 홀수: 홀수 카운트 추가
        if s[r] % 2:
            odd_cnt += 1
        # 짝수: 짝수 카운트 추가 및 정답 업데이트
        else:
            even_cnt += 1
            ans = max(ans, even_cnt)
        r += 1

print(ans)


'''
    왜 슬라이딩 윈도우(두 포인터)인가?
    
    "연속 구간"을 빠르게 탐색할 때 윈도우를 늘리고 줄이며 불필요한 재탐색 없이 한 번에 처리
    홀수(삭제) 카운트를 윈도우 내에서 실시간으로 관리 가능
    "최대 K개의 나쁜 요소를 허용한 채 좋은 요소(짝수)를 최대한 많이 모으기"가 슬라이딩 윈도우 패턴에 맞음
'''