// Jeff needs your help calculating his final balance after a series of deposits (D) and withdrawals (W) done to his bank account! He already has V in his bank account.
// Input
// Line 1: Two Integers V denoting his initial balance, and N denoting the amount of transactions he will make.
// Next N lines: One String Transaction denoting if he's depositing (D) or withdrawing (W), along with an integer Amount denoting the amount he is handling in the transaction.
// Output
// Output the final balance in Jeff's bank account.
// Constraints
// 0=<V,N,Amount=<5000
// Transaction = "W"||"D"

// Original code:
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
        int V = in.nextInt();
        int N = in.nextInt();
        for (int i = 0; i < N; i++) {
            String transaction = in.next();
            int amount = in.nextInt();
        }
    }
}
