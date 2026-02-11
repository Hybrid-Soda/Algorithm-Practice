class 짝수_홀수_개수_120824 {
    public int[] solution(int[] num_list) {
        int[] answer = new int[2];

        for (int n: num_list) {
            answer[n % 2]++;
        }

        return answer;
    }
}