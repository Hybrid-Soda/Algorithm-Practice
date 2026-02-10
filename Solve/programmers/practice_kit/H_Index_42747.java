package practice_kit;

import java.util.Arrays;

public class H_Index_42747 {

    public int solution(int[] citations) {
        int answer = 0;
        int n = citations.length;

        // 정렬
        Arrays.sort(citations);

        // H-Index 구하기
        int idx = 0;
        for (int h = 0; h < citations[n - 1]; h++) {
            while (h > citations[idx]) idx++;
            if (n - idx < h) break;
            answer = h;
        }

        return answer;
    }
}
