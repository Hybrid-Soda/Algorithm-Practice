// 12918 문자열 다루기 기본


class 문자열_다루기_기본_12918 {
    public boolean solution(String s) {
        if (s.length() == 4 || s.length() == 6) {
            return s.matches("(^[0-9]*$)");
        }
        return false;
    }
}
// class Solution {
//     public boolean solution(String s) {
//         int sLen = s.length();
        
//         if (sLen != 4 && sLen != 6) return false;

//         try {
//             int x = Integer.parseInt(s);
//             return true;
//         } catch (NumberFormatException e) {
//             return false;
//         }
//     }
// }