// 87389 나머지가 1이 되는 수 찾기

class Solution {
    public int solution(int n) {
        for (int i = 2; i < (int)(Math.sqrt(n)) + 1; i++) {
            if (n % i == 1) return i;
        }
        return n-1;
    }
}