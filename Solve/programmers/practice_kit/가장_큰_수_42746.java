package practice_kit;

import java.util.Arrays;

public class 가장_큰_수_42746 {

    public String solution(int[] numbers) {
        // 문자열로 이루어진 배열로 수정
        String[] arr = new String[numbers.length];
        for (int i = 0; i < numbers.length; i++)
            arr[i] = String.valueOf(numbers[i]);

        // 정렬
        Arrays.sort(arr, (a, b) -> (b + a).compareTo(a + b));

        // 문자 합치기
        String answer = "";
        for (String s : arr) answer += s;

        // 0 예외처리
        return answer.charAt(0) == '0' ? "0" : answer;
    }
}
