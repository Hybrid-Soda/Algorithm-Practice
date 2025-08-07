// 12940 최대공약수와 최소공배수

class Solution {
    public int[] solution(int n, int m) {
        return new int[] {gcd(n, m), lcm(n, m)};
    }

    // 최대 공약수
    private int gcd(int n, int m) {
        while (m > 0) {
            int t = n;
            n = m;
            m = t % m;
        }
        return n;
    }

    // 최소 공배수
    private int lcm(int n, int m) {
        return n * m / gcd(n, m);
    }
}