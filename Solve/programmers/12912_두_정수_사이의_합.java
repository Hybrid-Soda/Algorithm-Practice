// 12912 두 정수 사이의 합

class Solution {
    public long solution(int a, int b) {
        return sum(Math.min(a, b), Math.max(a, b));
    }

    private long sum(long a, long b) {
        return (b - a + 1) * (a + b) / 2;
    }
}