import java.io.*;
import java.util.*;
import java.util.concurrent.*;

public class DataTypes {
    private static void mainDataTypes(String[] args) throws IOException {
        /// 기본 자료형
        // 논리형
        boolean boolean1 = true;

        // 정수형
        byte byte1 = Byte.parseByte("10");             // 1byte
        short short1 = Short.parseShort("10");         // 2byte
        int int1 = Integer.parseInt("10");             // 4byte
        long long1 = Long.parseLong("10");             // 8byte

        // 실수형
        float float1 = Float.parseFloat("10.1");       // 4byte
        double double1 = Double.parseDouble("10.1");   // 8byte

        // 문자형
        char char1 = 'c';

        /// 참조 자료형
        // 문자열
        String string1 = "string";

        // 배열
        int[] array1 = new int[5];

        // 컬렉션 - List
        List<Object> aL1 = new ArrayList<>();   // 동적 배열, 조회에 좋음, 메모리 효율 높음
        List<Object> lL1 = new LinkedList<>();  // 이중 연결, 수정에 좋음, 메모리 효율 낮음

        // 컬렉션 - Set
        Set<Object> hS1 = new HashSet<>();                 // 순서 보장 x, 정렬 x, 가장 빠른 중복 제거
        Set<Object> tS1 = new TreeSet<>();                 // 순서 보장 x, 정렬 o, 자동 정렬 (red-black tree)
        Set<Object> lHS1 = new LinkedHashSet<>();          // 순서 보장 o, 정렬 x, 삽입 순서 유지
        Set<Object> cSLS1 = new ConcurrentSkipListSet<>(); // 순서 보장 x, 정렬 o, 동시성 + 정렬

        // 컬렉션 - Queue
        Queue<Object> pQ1 = new PriorityQueue<>();          // FIFO x, 우선순위 o, 양방향 x, heap
        Queue<Object> aD1 = new ArrayDeque<>();             // FIFO o, 우선순위 x, 양방향 o, 원형배열
        Queue<Object> lL2 = new LinkedList<>();             // FIFO o, 우선순위 x, 양방향 o, 이중 연결 리스트
        Queue<Object> cLQ1 = new ConcurrentLinkedQueue<>(); // FIFO o, 우선순위 x, 양방향 o, 동시성

        // 컬렉션 - Map
        Map<Object, Object> hM1 = new HashMap<>();            // 순서 보장 x, 정렬 x, 기본 맵
        Map<Object, Object> tM1 = new TreeMap<>();            // 순서 보장 x, 정렬 o, 키 기준 정렬
        Map<Object, Object> lHM1 = new LinkedHashMap<>();     // 순서 보장 o, 정렬 x, 순서 유지
        Map<Object, Object> cHM1 = new ConcurrentHashMap<>(); // 순서 보장 x, 정렬 x, 동시성
    }
}