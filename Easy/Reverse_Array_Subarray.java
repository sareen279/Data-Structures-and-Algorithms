//Reverse array in groups.
//Given an array arr[] of positive integers of size N. Reverse every sub-array of K group elements.

import java.io.*;
import java.util.*;

public static ArrayList<Integer> reverseInGroups(ArrayList<Integer> mv, int n, int k) {
        //n -> length of list, k -> length of subarray, mv -> arraylist
        int i = 0;
        int l;
        while(i < n)
        {
            if(n <= i+k)
                l = n-1;
            else
		l = i+k-1;
	    for(int j = i;j < l;j++,l--)
	    {
		int temp = mv.get(j);
		mv.set(j,mv.get(l));
		mv.set(l,temp);
	    }
	    i += k;
	}
	return mv;
}
