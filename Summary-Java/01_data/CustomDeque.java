public interface CustomDeque<E> {
    // 앞에 원소 삽입
    void addFirst(E e);

    // 뒤에 원소 삽입
    void addLast(E e);

    // 앞 원소 제거
    E pollFirst();

    // 뒤 원소 제거
    E pollLast();

    // 앞 원소 조회
    E peekFirst();

    // 뒤 원소 조회
    E peekLast();

    // 포함 체크
    boolean contains(Object o);

    // 크기 체크
    int size();

    // 비어있는지 체크
    boolean isEmpty();
}
