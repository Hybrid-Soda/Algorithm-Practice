class Solution {
    public int[] solution(int[] num_list, int n) {
        int flag = num_list.length % n == 0 ? 0 : 1;
        int[] answer = new int[num_list.length / n + flag];
        for (int i = 0; i < num_list.length / n + flag; i++) {
            answer[i] = num_list[i*n];
        }
        return answer;
    }
}