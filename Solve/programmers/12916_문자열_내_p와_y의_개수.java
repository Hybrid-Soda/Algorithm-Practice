// 12916 문자열 내 p와 y의 개수

class Solution {
    boolean solution(String s) {
        int term = 0;

        for (char chr: s.toLowerCase().toCharArray()) {
            if (chr == 'p') {
                term++;
            } else if (chr == 'y') {
                term--;
            }
        }

        return term == 0;
    }
}