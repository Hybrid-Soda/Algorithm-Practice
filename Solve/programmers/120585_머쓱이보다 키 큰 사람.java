class 머쓱이보다_키_큰_사람_120585 {
    public int solution(int[] array, int height) {
        int answer = 0;

        for (int h: array) {
            if (height < h) {
                answer += 1;
            }
        }

        return answer;
    }
}