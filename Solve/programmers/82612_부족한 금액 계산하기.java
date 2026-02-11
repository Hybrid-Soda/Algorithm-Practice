// 82612 부족한 금액 계산하기

class 부족한_금액_계산하기_82612 {
    public long solution(int price, int money, int count) {
        return Math.max(((long) price * count * (count + 1) / 2) - money, 0);
    }
}