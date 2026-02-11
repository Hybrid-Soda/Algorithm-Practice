// 86051 없는 숫자 더하기

import java.util.Arrays;

class 없는숫자_더하기_86051 {
    public int solution(int[] numbers) {
        return 45-Arrays.stream(numbers).sum();
    }
}