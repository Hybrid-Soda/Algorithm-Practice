class Solution {
    public String solution(String my_string) {
        String answer = "";

        for (char chr: my_string.toCharArray()) {
            answer = chr + answer;
        }

        return answer;
    }
}

// class Solution {
//     public String solution(String myString) {
//         return new StringBuilder(myString).reverse().toString();
//     }
// }