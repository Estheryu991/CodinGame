import java.util.*;
import java.io.*;
import java.math.*;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/
class Solution {

    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int x = in.nextInt();
        int sum=0; 

        for (int i=1 ; i< x; i++){
            sum+= Math.pow(n,i);
        }
        System.out.println(sum+1);
    }
}
