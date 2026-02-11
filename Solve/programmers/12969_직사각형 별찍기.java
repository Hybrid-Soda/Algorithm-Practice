// 12969 직사각형 별찍기

import java.util.Scanner;

class 직사각형_별찍기_12969 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();

        for (int i = 0; i < b; i++) {
            System.out.println("*".repeat(a));
        }
    }
}