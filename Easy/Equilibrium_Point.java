//Equilibrium Point
//Given an array A of N positive numbers. The task is to find the first Equilibium Point in the array. 
//Equilibrium Point in an array is a position such that the sum of elements before it is equal to the sum of elements after it.
//The output should be based on 1 based indexing.

import java.io.*;
import java.util.*;

class Equilibrium_Point
{
	public static void main(String[] args)
	{
		int arr[] = {1,3,5,2,2};
		int n = arr.length;
		int ct = 0;
		int lct = 0;
		for(int i = 0;i < n;i++)
		{
 	   		ct+=arr[i];
		}
		int ind = equi(arr,n,ct,lct);
		System.out.println(ind);
	}
	public static int equi(int[] arr, int n, int ct, int lct)
	{
		for(int i = 0;i < n;i++)
                {
			ct -= arr[i];
                        if(lct == ct)
                        	return (i+1);
                        lct += arr[i];
                }
                return -1;
	}
}
