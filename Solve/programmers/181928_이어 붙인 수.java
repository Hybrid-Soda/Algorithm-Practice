class 이어_붙인_수_181928 {
    public int solution(int[] num_list) {
        int odd = 0;
        int even = 0;
        for (int num: num_list) {
            if (num % 2 == 0) {
                even = even * 10 + num;
            } else {
                odd = odd * 10 + num;
            }
        }
        return odd + even;
    }
}