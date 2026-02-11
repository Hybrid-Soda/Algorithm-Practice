// 12943 콜라츠 추측

class 콜라츠_추측_12943 {
    public int solution(long num) {
        
        for (int i = 0; i < 500; i++) {
            
            if (num == 1) return i; 
            
            num = (num % 2 == 0) ? num/2 : num*3+1;
        }

        return -1;
    }
}