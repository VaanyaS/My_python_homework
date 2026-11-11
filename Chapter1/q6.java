package Chapter1;

 /**
 * @author (your name)
 * @version (a version number or a date)
 */
import java.util.Scanner;

public class q6 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int arr[] = new int[20];
        int i=0;
        System.out.println("Enter 20 numbers:");
        for (i=0;i<20;i++){
            arr[i] = sc.nextInt();
        }
        System.out.println("Consecuutive numbers are:");
        for (i=0;i<19;i++){
            if (arr[i + 1] - arr[i] == 1) {
                System.out.println(arr[i] + " and " + arr[i + 1]);
            }
        }}
}
