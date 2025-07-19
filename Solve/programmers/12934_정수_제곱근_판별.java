// 12934 정수 제곱근 판별

class Solution {
    public long solution(long n) {
        double sqrtN = Math.sqrt(n);

        if (sqrtN % 1 == 0) {
            return (long) Math.pow(sqrtN + 1, 2);
        }

        return -1;
    }
}