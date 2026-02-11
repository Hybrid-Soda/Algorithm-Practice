// 12903 가운데 글자 가져오기

class 가운데_글자_가져오기_12903 {
    public String solution(String s) {
        int len = s.length();
        
        if (len % 2 == 0) {
            return s.substring(len/2-1, len/2+1);
        } else {
            return s.substring(len/2, len/2+1);
        }
    }
}