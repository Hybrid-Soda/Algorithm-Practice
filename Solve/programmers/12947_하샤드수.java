// 12947 하샤드 수

class 하샤드수_12947 {
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