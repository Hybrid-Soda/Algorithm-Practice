// 12935 제일 작은 수 제거하기

import java.util.Arrays;

class 제일_작은_수_제거하기_12935 {
    public int[] solution(int[] arr) {

        if (arr.length <= 1) {
            return new int[] {-1};
        }

        int min = Arrays.stream(arr).min().getAsInt();

        return Arrays.stream(arr).filter(num -> num != min).toArray();
    }
}