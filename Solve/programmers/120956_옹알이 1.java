class 옹알이_1_120956 {
    public int solution(String[] babbling) {
        int answer = 0;

        for (String str: babbling) {
            answer += check(str);
        }

        return answer;
    }

    private int check(String str) {
        String[] able = new String[] {"aya", "ye", "woo", "ma"};
        
        for (String word: able) {
            if (str.contains(word)) {
            str = str.replace(word, " ");
            }
        }
        
        str = str.trim();
        return str.isEmpty() ? 1 : 0;
    }
}