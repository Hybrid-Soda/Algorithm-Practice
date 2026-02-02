package practice_kit;

import java.util.Arrays;

public class 모의고사_42840 {

    public int[] solution(int[] answers) {
        int[] count = new int[3];
        int[] pattern1 = new int[] {1, 2, 3, 4, 5}; // 5
        int[] pattern2 = new int[] {2, 1, 2, 3, 2, 4, 2, 5}; // 8
        int[] pattern3 = new int[] {3, 3, 1, 1, 2, 2, 4, 4, 5, 5}; // 10

        // 채점
        for (int i = 0; i < answers.length; i++) {
            count[0] += pattern1[i % 5] == answers[i] ? 1 : 0;
            count[1] += pattern2[i % 8] == answers[i] ? 1 : 0;
            count[2] += pattern3[i % 10] == answers[i] ? 1 : 0;
        }

        // 최다득점자 파악
        int max = Arrays.stream(count).max().orElse(0);
        return Arrays.stream(new int[] {1, 2, 3}).filter(i -> count[i - 1] == max).toArray();
    }
}
