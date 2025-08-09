// 147355 크기가 작은 부분 문자열

class Solution {
    public int solution(String t, String p) {
        int answer = 0;
        for (int i = 0; i <= t.length() - p.length(); i++) {
            if (Long.valueOf(t.substring(i, i+p.length())) <= Long.valueOf(p)) {
                answer++;
            }
        }
        return answer;
    }
}