// 12917 문자열 내림차순으로 배치하기

import java.util.Arrays;
import java.util.Collections;

class 문자열_내림차순으로_배치하기_12917 {
    public String solution(String s) {
        String[] str = s.split("");
        Arrays.sort(str, Collections.reverseOrder());
        
        return String.join("", str);
    }
}