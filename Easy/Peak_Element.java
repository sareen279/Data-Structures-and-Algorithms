//Peak element
//Given an array A of N integers. The task is to find a peak element in it in O( log N ) .
//An array element is peak if it is not smaller than its neighbours. For corner elements, we need to consider only one neighbour.
//Expected Time Complexity: O(log N)
//Expected Auxiliary Space: O(1)

import java.util.*;
import java.io.*;

class Peak_Element
{
	public static void main(String[] args)
	{
		int a[] = {1,2,3,4,5,6,4};
	        int n = a.length;
        	int st = 0;
        	int end = n - 1;
        	int mid = (st + end) / 2;
        	if(n == 1)
        	{
        	    System.out.println("0");
        	    System.exit(0);
        	}
		if(n == 2)
	        {
            	if(a[0] <= a[1])
                	System.out.println("1");
            	else
                	System.out.println("0");
            	System.exit(0);
        	}
        	while(a[mid - 1] > a[mid] || a[mid + 1] > a[mid])
        	{
            		if(a[mid - 1] > a[mid])
			        end = mid;
            		else
                		st = mid + 1;
            		mid = (st + end) / 2;
            		if((mid == 0 && a[mid + 1] <= a[mid]) || (mid == n-1 && a[mid - 1] <= a[mid]))
            		{
                		System.out.println(mid);
                		System.exit(0);
            		}
		}
		System.out.println(mid);
	}
}
