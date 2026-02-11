package practice_kit;

import java.util.Arrays;

public class 사칙연산_1843 {

    public int solution(String arr[]) {
        // dp[i][j]: i번째 숫자부터 j번째 숫자까지 만들 수 있는 최대값/최소값
        int n = arr.length / 2 + 1;
        int[][] maxDp = new int[n][n];
        int[][] minDp = new int[n][n];

        // 초기화
        for (int i = 0; i < n; i++) {
            maxDp[i][i] = Integer.parseInt(arr[2 * i]);
            minDp[i][i] = Integer.parseInt(arr[2 * i]);
        }

        // 구간 길이
        for (int len = 1; len < n; len++) {
            // 구간 내 시작 숫자 인덱스
            for (int i = 0; i < n - len; i++) {
                // 구간 내 끝 숫자 인덱스
                int j = i + len;
                // 초기화
                maxDp[i][j] = Integer.MIN_VALUE;
                minDp[i][j] = Integer.MAX_VALUE;

                // 분할점 k 탐색: 구간 [i, j]를 [i, k], [k+1, j]로 나눔
                for (int k = i; k < j; k++) {
                    int maxLeft = maxDp[i][k]; // 분할점까지 제작 숫자 중 최댓값
                    int minLeft = minDp[i][k]; // 분할점까지 제작 숫자 중 최솟값
                    int maxRight = maxDp[k + 1][j]; // 분할점 이후 제작 숫자 중 최댓값
                    int minRight = minDp[k + 1][j]; // 분할점 이후 제작 숫자 중 최솟값
                    System.out.println("i- " + i + " / " + "j- " + j + " / " + "k- " + k);
                    System.out.println("left: " + maxLeft + ", " + minLeft);
                    System.out.println("right: " + maxRight + ", " + minRight);

                    // 합과 차에 따라 달라짐
                    String operator = arr[2 * k + 1];
                    if (operator.equals("+")) {
                        maxDp[i][j] = Math.max(maxDp[i][j], maxLeft + maxRight);
                        minDp[i][j] = Math.min(minDp[i][j], minLeft + minRight);
                    } else {
                        maxDp[i][j] = Math.max(maxDp[i][j], maxLeft - minRight);
                        minDp[i][j] = Math.min(minDp[i][j], minLeft - maxRight);
                    }
                }

                System.out.println("---");
                for (int[] row : maxDp) {
                    System.out.println(Arrays.toString(row));
                }
                System.out.println("---");
                for (int[] row : minDp) {
                    System.out.println(Arrays.toString(row));
                }
                System.out.println("----------------------------");
            }
        }

        return maxDp[0][n - 1];
    }

    public void start(String[] args) {
        int maxVal = solution(new String[]{"5", "-", "3", "+", "1", "+", "2", "-", "4"});
        System.out.println(maxVal);
    }
}
