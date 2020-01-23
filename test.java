import java.io.*;
import java.util.*;
public class test{
    static void myProcess(String s){
        String er = "[ '.,?!]+";
        String[] r = s.split(er);
        int i = 0;
        while(r[i]!="\0"){
            i++;
        }
        System.out.println(i);
        for(int j=0;j<i;j++) System.out.println(r[j]);
    }
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.nextLine();
        // Write your code here.
        try{
            myProcess(s);
        }
        catch(Exception e)
        {
            System.out.println("Exception program");
        }
        scan.close();
    }
}
