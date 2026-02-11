// 12944 평균 구하기

import java.util.Arrays;

class 평균_구하기_12944 {
    public double solution(int[] arr) {
        return Arrays.stream(arr).average().getAsDouble();
    }
}