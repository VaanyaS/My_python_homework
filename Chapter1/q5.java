package Chapter1;


/**
 * Write a description of class q5 here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class q5
{
    public static void main(String[] args){
        int i=0;
        int sum=0;
        int avg=0;
        int m[]={23,31,44,56,72,55};
        
        for(i=0;i<=5;i++)
            {sum+=m[i];};
            
        System.out.println(sum);
        avg=sum/6;
        System.out.println(avg);
        
            
        
    }
}