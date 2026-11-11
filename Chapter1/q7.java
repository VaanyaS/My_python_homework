package Chapter1;

/**
 * Write a description of class q7 here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
import java.util.Scanner;
public class q7 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int a=0;
        int i=0;
        double arr[]= new double[20];
        
        System.out.println("Enter 20 temps on degrees F:");
        for (i=0;i<20;i++){
            arr[i] = sc.nextDouble();
        }

        System.out.println("Temperatures in Celsius:");
        for(a=0;a<20;a++) {
            arr[a]=(arr[a]-32)*5.0/9.0;
            System.out.println(arr[a]);
        }
    }
}
