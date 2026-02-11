// 70128 내적

class 내적_70128 {
    public int solution(int[] a, int[] b) {
        int dot = 0;

        for (int i = 0; i < a.length; i++) {
            dot += a[i] * b[i];
        }

        return dot;
    }
}


// import java.util.stream.IntStream;

// class Solution {
//     public int solution(int[] a, int[] b) {
//         return IntStream.range(0, a.length).map(idx -> a[idx] * b[idx]).sum();
//     }
// }