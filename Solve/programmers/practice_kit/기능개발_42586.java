package practice_kit;

import java.util.ArrayDeque;

public class 기능개발_42586 {

    public ArrayDeque<Integer> solution(int[] progresses, int[] speeds) {
        ArrayDeque<Integer> answer = new ArrayDeque<>();
        ArrayDeque<Integer> daysLeft = new ArrayDeque<>();

        // 각 작업마다 남은 일수 구하기
        for (int i = 0; i < progresses.length; i++) {
            int left = (int) Math.ceil((double) (100 - progresses[i]) / speeds[i]);
            daysLeft.addLast(left);
        }

        // 순회하면서 큐에서 배포 작업 빼내고 작업 수 카운팅하기
        while (!daysLeft.isEmpty()) {
            int count = 1;
            int benchmark = daysLeft.removeFirst();

            // 뒤의 작업이 기준 작업의 일수와 같거나 작으면 같이 빼기
            while (!daysLeft.isEmpty() && benchmark >= daysLeft.getFirst()) {
                daysLeft.removeFirst();
                count++;
            }

            answer.add(count);
        }

        return answer;
    }
}
