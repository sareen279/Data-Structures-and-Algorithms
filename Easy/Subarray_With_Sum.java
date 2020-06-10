//Subarray with given sum
//Given an unsorted array A of size N of non-negative integers, find a continuous sub-array which adds to a given number S.
//Expected Time Complexity: O(N)
//Expected Auxiliary Space: O(1)
/*Input:
3
5 12
1 2 3 7 5
10 15
1 2 3 4 5 6 7 8 9 10
4 15
5 7 1 2*/
//Print the starting and ending index of the subarray with 1 indexing method

import java.util.*;
import java.lang.*;
import java.io.*;

class Subarray_With_Sum{
	public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int t = sc.nextInt();

        for (int i = 0; i < t; i++) {
            int n = sc.nextInt();
            int s = sc.nextInt();

            int[] m = new int[n];
            for (int j = 0; j < n; j++) {
                m[j] = sc.nextInt();
            }
            
            Subarray obj = new Subarray();
            obj.subarraySum(n, s, m);
            System.out.println();
        }
    }

}// } Driver Code Ends


class Subarray{
    
    // Function to find subarray with given sum
    static void subarraySum(int n, int s, int[] m) {
        int fl = 0,curr_sum = m[0], start = 0, i; 
  
        // Pick a starting point 
        for (i = 1; i <= n; i++) { 
            // If curr_sum exceeds the sum, 
            // then remove the starting elements 
            while (curr_sum > s && start < i - 1) { 
                curr_sum = curr_sum - m[start]; 
                start++; 
            } 
  
            // If curr_sum becomes equal to sum, 
            // then return true 
            if (curr_sum == s) { 
                int p = i; 
                System.out.print((start+1) + " " + p);
                fl = 1;
                break; 
            } 
  
            // Add this element to curr_sum 
            if (i < n) 
                curr_sum = curr_sum + m[i]; 
        }
        if(fl == 0)
            System.out.print("-1");
        // Your code here
        
    }
}
