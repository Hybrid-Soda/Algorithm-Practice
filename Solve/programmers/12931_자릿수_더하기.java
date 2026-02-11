// 12931 자릿수 더하기

class 자릿수_더하기_12931 {
    private int solution(int n) {
        int answer = 0;

        while (n > 0) {
            answer += n % 10;
            n /= 10;
        }

        return answer;
    }
}