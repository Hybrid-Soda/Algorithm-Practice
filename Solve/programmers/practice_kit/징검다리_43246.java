package practice_kit;

import java.util.Arrays;

public class 징검다리_43246 {

    /**
     * 핵심 : 구해야 할 것이 "각 지점 사이의 거리의 최솟값" 중에 가장 큰 값
     * -> "최솟값"의 가장 큰 값을 이분탐색으로 찾아야 함
     * */
    public int solution(int distance, int[] rocks, int n) {
        int answer = 0;
        Arrays.sort(rocks);

        // 이분탐색
        int start = 1;
        int end = distance;

        while (start <= end) {
            int mid = (start + end) / 2;

            // 만족하면 시작을 뒤로 땡김, 만족하지 않으면 끝을 앞으로 땡김
            if (getRemovedCnt(distance, rocks, mid) <= n) {
                answer = mid;
                start = mid + 1;
            } else {
                end = mid - 1;
            }
        }

        return answer;
    }

    // 최소 간격에 따른 제거 돌 카운트
    public int getRemovedCnt(int distance, int[] rocks, int minTerm) {
        int removeCnt = 0;
        int markPos = 0;

        for (int pos : rocks) {
            // 돌 사이 간격이 기준 간격 이상이면 패스, 미만이면 현재 돌 제거
            if (pos - markPos >= minTerm) {
                markPos = pos;
            } else {
                removeCnt++;
            }
        }
        if (distance - markPos < minTerm) removeCnt++;

        return removeCnt;
    }
}
