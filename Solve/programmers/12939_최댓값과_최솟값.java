// 12939 최댓값과 최솟값

class 최댓값과_최솟값_12939 {
    public String solution(String s) {
        String[] sList = s.split(" ");

        int maxV = Integer.MIN_VALUE;
        int minV = Integer.MAX_VALUE;

        for (String num : sList) {
            int n = Integer.parseInt(num);
            maxV = Math.max(maxV, n);
            minV = Math.min(minV, n);
        }

        String answer = minV + " " + maxV;
        return answer;
    }
}