package practice_kit;

import java.util.HashMap;

public class 의상_42578 {
    public int solution(String[][] clothes) {
        int answer = 1;
        HashMap<String, Integer> clothesMap = new HashMap<>();

        // 의류 종류의 개수를 해시에 저장
        for (String[] cloth: clothes) {
            int count = clothesMap.getOrDefault(cloth[1], 0);
            clothesMap.put(cloth[1], count + 1);
        }

        // 조합 계산
        for (int count: clothesMap.values()) {
            answer *= count + 1;
        }

        return answer - 1;
    }
}
