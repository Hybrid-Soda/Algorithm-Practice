// 68935 3진법 뒤집기

import java.util.ArrayList;

class _3진법_뒤집기_68935 {
    public int solution(int n) {
        return getDecimal(getReversedTernary(n));
    }

    private ArrayList getReversedTernary(int n) {
        ArrayList ternary = new ArrayList();
        
        while (n > 0) {
            ternary.add(n % 3);
            n /= 3;
        }

        return ternary;
    }

    private int getDecimal(ArrayList ternery) {
        int answer = 0;
        int exponent = ternery.size() - 1;

        for (int i = 0; i <= exponent; i++) {
            answer += (int) ternery.get(i) * Math.pow(3, exponent - i);
        }

        return answer;
    }
}