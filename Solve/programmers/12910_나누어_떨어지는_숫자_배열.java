// 12910 나누어 떨어지는 숫자 배열

import java.util.Arrays;

class Solution {
    public int[] solution(int[] arr, int divisor) {
        int[] answer = Arrays
            .stream(arr)
            .filter(num -> num % divisor == 0)
            .sorted()
            .toArray();

        return answer.length == 0 ? new int[]{-1} : answer;
    }
}