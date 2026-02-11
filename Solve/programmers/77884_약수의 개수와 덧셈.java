// 77884 약수의 개수와 덧셈

import java.util.stream.IntStream;

class 약수의_개수와_덧셈_77884 {
    public int solution(int left, int right) {
        int answer = 0;
        for (int num = left; num <= right; num++) {
            answer += getDivisorCount(num) % 2 != 0 ? num : -num;
        }
        return answer;
    }

    private int getDivisorCount(int num) {
        return (int) IntStream.range(1, num/2 + 1).filter(i -> num % i == 0).count();
    }
}

// for (int i=left;i<=right;i++) {
//     if (i % Math.sqrt(i) == 0) {  //제곱수인 경우 약수의 개수가 홀수
//         answer -= i;
//     } else {  //제곱수가 아닌 경우 약수의 개수가 짝수
//         answer += i;
//     }
// }