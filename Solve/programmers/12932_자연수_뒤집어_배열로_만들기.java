// 12932 자연수 뒤집어 배열로 만들기

import java.util.ArrayList;

class Solution {
    public ArrayList<Integer> solution(long n) {
        ArrayList<Integer> answer = new ArrayList<>();
        
        while (n > 0L) {
            // 형 변환 시 캐스팅 연산자 (int)가 나눗셈 연산자보다 결합 우선순위가 높다
            answer.add((int)(n % 10));
            n /= 10;
        }
        
        return answer;
    }
}