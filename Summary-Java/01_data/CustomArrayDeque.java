
public class CustomArrayDeque<E> implements CustomDeque<E> {

    transient Object[] elements;
    transient int head; // 앞 부분
    transient int tail; // 뒤 부분

    public CustomArrayDeque() {
        elements = new Object[16 + 1];
    }

    public CustomArrayDeque(int numElements) {
        int num;

        if (numElements < 1) {
            num = 1;
        } else if (numElements == Integer.MAX_VALUE) {
            num = Integer.MAX_VALUE;
        } else {
            num = numElements + 1;
        }

        elements = new Object[num];
    }

    // 인덱스 뒤로 이동
    private int inc(int i, int size) {
        if (++i >= size)
            i = 0;
        return i;
    }

    // 인덱스 앞으로 이동
    private int dec(int i, int size) {
        if (--i < 0)
            i = size - 1;
        return i;
    }

    private int sub(int i, int j, int modulus) {
        if ((i -= j) < 0)
            i += modulus;
        return i;
    }

    @SuppressWarnings("unchecked")
    private E elementAt(Object[] es, int i) {
        return (E) es[i];
    }

    @Override
    public void addFirst(E e) {
        if (e == null)
            throw new NullPointerException();
        final Object[] es = elements;
        es[head = dec(head, es.length)] = e;
    }

    @Override
    public void addLast(E e) {
        if (e == null)
            throw new NullPointerException();
        final Object[] es = elements;
        es[tail = inc(tail, es.length)] = e;
    }

    @Override
    public E pollFirst() {
        final Object[] es;
        final int h;
        E e = elementAt(es = elements, h = head);

        if (e != null) {
            es[h] = null;
            head = inc(h, es.length);
        }
        return e;
    }

    @Override
    public E pollLast() {
        final Object[] es;
        final int t;
        E e = elementAt(es = elements, t = dec(tail, es.length));

        if (e != null) {
            es[tail = t] = null;
        }
        return e;
    }

    @Override
    public E peekFirst() {
        return elementAt(elements, head);
    }

    @Override
    public E peekLast() {
        final Object[] es;
        return elementAt(es = elements, dec(tail, es.length));
    }

    @Override
    public boolean contains(Object o) {
        if (o != null) {
            final Object[] es = elements;

            // 원형 큐 순회
            for (int i = head, end = tail, to = (i <= end) ? end : es.length;;i = 0, to = end) {
                for (; i < to; i++) {
                    // 일치하는 원소를 찾으면 true 반환
                    if (o.equals(es[i]))
                        return true;
                }
                if (to == end) break;
            }
        }
        return false;
    }

    @Override
    public int size() {
        return sub(tail, head, elements.length);
    }

    @Override
    public boolean isEmpty() {
        return tail == head;
    }
}
