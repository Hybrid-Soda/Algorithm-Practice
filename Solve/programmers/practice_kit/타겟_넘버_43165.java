package practice_kit;

public class 타겟_넘버_43165 {

    public int solution(int[] numbers, int target) {
        return dfs(numbers, target, 0, 0);
    }

    public int dfs(int[] numbers, int target, int idx, int sum) {
        // 최종까지 가면 숫자를 비교하여 카운트 or 무시
        if (idx >= numbers.length)
            return (sum == target) ? 1 : 0;

        // depth를 늘려가며 양/음 으로 합산
        int a = dfs(numbers, target, idx + 1, sum + numbers[idx]);
        int b = dfs(numbers, target, idx + 1, sum - numbers[idx]);

        // 카운트 반환
        return a + b;
    }
}
