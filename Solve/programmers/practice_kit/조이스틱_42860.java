package practice_kit;

public class 조이스틱_42860 {

    public int solution(String name) {
        int n = name.length();
        int colMove = 0;
        int rowMove = n - 1;

        for (int i = 0; i < n; i++) {
            char c = name.charAt(i);

            // 열 이동 구하기
            colMove += Math.min(c - 'A', 'Z' - c + 1);

            // 연속된 A 건너뛰기
            int nextIdx = i + 1;
            while (nextIdx < n && name.charAt(nextIdx) == 'A') nextIdx++;

            // 오른쪽 먼저
            rowMove = Math.min(rowMove, i * 2 + n - nextIdx);
            // 왼쪽 먼저
            rowMove = Math.min(rowMove, i + (n - nextIdx) * 2);
        }

        return colMove + rowMove;
    }
}
