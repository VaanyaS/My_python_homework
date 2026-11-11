package Chapter1;
import java.util.Scanner;


/**
 Skipped Q8 UPDATE!!!!
 */
public class q9 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int arr[] = new int[20];
        int i=0;
        int sofeven=0;
        int sofodd=0;
        System.out.println("Enter 20 numbers:");
        for (i=0;i<20;i++){
            arr[i] = sc.nextInt();
        }
        
        for(i=0;i<=19;i++){
            if (arr[i]%2==0) {
                sofeven+=arr[i];
            }
            else{
                sofodd+=arr[i];
            }
        }
        System.out.println("The sum of all even numbers is: "+sofeven);
        System.out.println("TYhe sum of all odd numbers is: " +sofodd);
    }
}