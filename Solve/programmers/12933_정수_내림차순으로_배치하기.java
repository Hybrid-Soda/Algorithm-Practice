// 12933 정수 내림차순으로 배치하기

import java.util.Comparator;
import java.util.stream.Collectors;
import java.util.stream.Stream;

class 정수_내림차순으로_배치하기_12933 {
    public long solution(long n) {
        
        // String 배열로 변환
        return Stream.of(String.valueOf(n).split(""))
                // 역순으로 정렬
                .sorted(Comparator.reverseOrder())
                // Long으로 변환
                .collect(Collectors.collectingAndThen(Collectors.joining(), Long::parseLong));
    }
}