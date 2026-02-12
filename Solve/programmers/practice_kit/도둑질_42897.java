package practice_kit;

public class 도둑질_42897 {

    public int solution(int[] money) {
        int n = money.length;
        int case1 = rob(money, 0, n - 2); // 첫번째 집 강탈 o
        int case2 = rob(money, 1, n - 1); // 첫번째 집 강탈 x
        return Math.max(case1, case2);
    }

    private int rob(int[] money, int start, int end) {
        int prev1 = 0; // i-1
        int prev2 = 0; // i-2

        for (int i = start; i <= end; i++) {
            int current = Math.max(prev1, prev2 + money[i]);
            prev2 = prev1;
            prev1 = current;
        }

        return prev1;
    }
}
