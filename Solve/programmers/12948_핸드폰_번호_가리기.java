// 12948 핸드폰 번호 가리기

class 핸드폰_번호_가리기_12948 {
    // 주어진 핸드폰 번호의 뒷 4자리를 제외한 모든 숫자를 '*'로 가려 반환
    public String solution(String phone_number) {
        return phone_number.replaceAll(".(?=.{4})", "*");
    }
}