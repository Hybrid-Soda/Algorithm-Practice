// 12922 수박수박수박수박수박수?

class 수박수박수박수박수박수_12922 {
    public String solution(int n) {
        return "수박".repeat(n/2 + 1).substring(0, n);
    }
}