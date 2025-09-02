class Solution {
    public double solution(int[] numbers) {
        double sum = 0;
        for (int number : numbers) {
            sum += number;
        }
        return sum / numbers.length;
    }
}


// import java.util.Arrays;

// class Solution {
//     public double solution(int[] numbers) {
//         return Arrays.stream(numbers).average().orElse(0);
//     }
// }