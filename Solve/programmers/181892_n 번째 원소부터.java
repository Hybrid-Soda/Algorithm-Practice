import java.util.Arrays;

class n_번째_원소부터_181892 {
    public int[] solution(int[] num_list, int n) {
        int[] answer = Arrays.copyOfRange(num_list, n-1, num_list.length);
        return answer;
    }
}