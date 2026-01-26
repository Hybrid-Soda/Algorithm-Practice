package practice_kit;

import java.util.Arrays;

public class 전화번호_목록_42577 {
    public boolean solution(String[] phone_book) {
        // 정렬
        Arrays.sort(phone_book);

        // 순회하면서 이전 글자와 다음 글자 확인
        for (int i = 0; i < phone_book.length - 1; i++) {
            // 접두어이면 false
            if (phone_book[i + 1].startsWith(phone_book[i]))  {
                return false;
            }
        }
        return true;
    }
}
