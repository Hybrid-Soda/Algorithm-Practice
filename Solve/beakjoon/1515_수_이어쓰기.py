# 1515 수 이어 쓰기 / 구현, 그리디 알고리즘, 문자열, 브루트포스 알고리즘

nums = input()
len_nums = len(nums)
idx, ans = 0, 0

# nums의 모든 문자를 검사할 때까지 반복
while idx < len(nums):
    ans += 1
    
    for s in str(ans):
        # 숫자를 하나 맞히면 다음 수로 넘어간다
        if idx < len_nums and nums[idx] == s:
            idx += 1

print(ans)