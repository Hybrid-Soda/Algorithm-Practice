import java.util.Arrays;

public class Sort {
    private static void change(int[] arr, int i, int j) {
        int temp = arr[j];
        arr[j] = arr[i];
        arr[i] = temp;
    }

    // 인접 원소 교환 반복 방식
    public static void bubbleSort(int[] arr, int n) {
        for (int i = 0; i < n; i++) {
            for (int j = n - 1; j > i; j--) {
                if (arr[j] < arr[j - 1]) {
                    change(arr, j, j - 1);
                }
            }
        }
        System.out.println(Arrays.toString(arr));
    }

    // 최솟값 선택 후 교환 방식
    public static void selectionSort(int[] arr, int n) {
        for (int i = 0; i < n - 1; i++) {
            int minIdx = i;
            for (int j = i + 1; j < n; j++) {
                if (arr[minIdx] > arr[j]) {
                    minIdx = j;
                }
            }
            change(arr, i, minIdx);
        }
        System.out.println(Arrays.toString(arr));
    }
}