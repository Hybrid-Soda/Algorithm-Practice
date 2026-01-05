import java.util.ArrayList;
import java.util.EmptyStackException;

public class Stack<E> {

    private final ArrayList<E> stack = new ArrayList<>();

    // 원소 추가
    public void push(E elem) {
        stack.add(elem);
    }

    // 원소 제거
    public E pop() {
        int len = size();

        E elem = peek();
        stack.remove(len - 1);

        return elem;
    }

    // 말단 원소 조회
    public E peek() {
        int len = size();

        if (len == 0) {
            throw new EmptyStackException();
        }

        return stack.get(len - 1);
    }

    // 비어있는지 체크
    public boolean isEmpty() {
        return size() == 0;
    }

    // 크기 체크
    public int size() {
        return stack.size();
    }
}