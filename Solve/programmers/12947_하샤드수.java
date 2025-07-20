// 12947 하샤드 수

class Solution {
    public boolean solution(int x) {
        double dividend = x;
        int divisor = 0;

        while (x > 0) {
            divisor += x % 10;
            x /= 10;
        }

        return (dividend / divisor) % 1 == 0;
    }
}