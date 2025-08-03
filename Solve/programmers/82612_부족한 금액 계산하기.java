// 82612 부족한 금액 계산하기

class Solution {
    public long solution(int price, int money, int count) {
        return Math.max(((long) price * count * (count + 1) / 2) - money, 0);
    }
}