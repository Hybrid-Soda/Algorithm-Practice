package practice_kit;

import java.util.PriorityQueue;

public class 더_맵게_42626 {

    public int solution(int[] scoville, int K) {
        int answer = 0;

        // 우선순위 큐에 음식 추가
        PriorityQueue<Integer> queue = new PriorityQueue<>();
        for (int food : scoville)
            queue.add(food);

        while (true) {
            int food1 = queue.remove();

            // 가장 스코빌 지수가 낮은 음식과 기준 스코빌 비교
            if (food1 >= K)
                return answer;

            // 더이상 음식을 섞을 수 없으면 -1 반환
            if (queue.isEmpty())
                return -1;

            // 음식 섞기
            int food2 = queue.remove();
            queue.add(food1 + 2 * food2);
            answer++;
        }
    }
}
