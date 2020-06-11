//Kadane's Algorithm
//Given an array arr of N integers. Find the contiguous sub-array with maximum sum.
//Expected Time Complexity: O(N)
//Expected Auxiliary Space: O(1)
//The array contains positive as well as negative numbers.

import java.util.*;
import java.io.*;
import java.lang.*;

public class Kadane_Algorithm
{
	public static void main(String[] args)
	{
		int arr[] = {1,2,3,-2,5};
		int n = arr.length;
		int gsum = arr[0];
		int sum = arr[0];
		for(int i = 1;i < n;i++)
		{
			sum = Math.max(arr[i],sum + arr[i]);
			if(gsum < sum)
				gsum = sum;
		}
		System.out.println("Maximum sum possible is " + gsum);
	}
}
