package Chapter1;

import java.util.Scanner;

public class q10 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);        
        
        int arr[] = new int[20];
        int i = 0;        
        System.out.println("Enter 20 numbers:");
        for (i = 0; i < 20; i++) {
            arr[i] = sc.nextInt();
        }
        
        System.out.println("Primne numbers are:");
        for (i = 0; i < 20; i++) {
            int factors = 0; 
            for (int j = 1; j <= arr[i]; j++) {
                if (arr[i] % j == 0) {
                    factors++; 
                }
            }            if (factors == 2) {
                System.out.println(arr[i]);
            }
        }
            }
}

