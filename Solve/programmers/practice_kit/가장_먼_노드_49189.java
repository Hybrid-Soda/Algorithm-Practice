package practice_kit;

import java.util.ArrayDeque;
import java.util.ArrayList;

public class 가장_먼_노드_49189 {

    // 목표: 1번 노드로부터 가장 멀리 떨어진 노드의 개수 구하기
    public int solution(int n, int[][] edge) {
        int answer = 0;

        // 그래프 생성
        ArrayList<ArrayList<Integer>> graph = new ArrayList<>();
        for (int i = 0; i <= n; i++) {
            graph.add(new ArrayList<>());
        }
        for (int[] pair : edge) {
            graph.get(pair[0]).add(pair[1]);
            graph.get(pair[1]).add(pair[0]);
        }

        // bfs로 그래프를 돌며 각 노드까지 가는 최단거리 계산 -> 저장할 것: 노드번호, 거리
        int maxDist = 0;
        int[] distance = new int[n + 1];
        ArrayDeque<Integer> queue = new ArrayDeque<>();
        queue.add(1);
        while (!queue.isEmpty()) {
            int now = queue.pop();

            // 가장 멀리 떨어진 노드의 개수 구하기
            if (maxDist < distance[now]) {
                maxDist = distance[now];
                answer = 1;
            } else {
                answer++;
            }

            // 다음 노드 체크
            for (int next : graph.get(now)) {
                if (next != 1 && distance[next] == 0) {
                    queue.add(next);
                    distance[next] += distance[now] + 1;
                }
            }
        }

        return answer;
    }
}
