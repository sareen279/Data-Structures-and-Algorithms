//Locate the occurrence of String 'target' in String 'str'.
//It should return the first occurrence or if not then '-1'.
//Expected TIme complexity - O(|target|*|str|)

import java.io.*;
import java.util.*;

class String_in_String
{
	public static void main(String[] args)
	{
	String str = "GeeksForGeeks";
        String target = "eks";
        boolean fl = true;
        for(int i = 0;i <= (str.length() - target.length());i++)
        {
            if(str.charAt(i) == target.charAt(0))
            {
                fl = true;
                for(int j = i+1,k = 1;k < target.length();j++,k++)
                {
                    if(str.charAt(j) != target.charAt(k))
                        fl = false;
                }
                if(fl)
		{
		    System.out.println(i);
		    System.exit(0);
		}
            }
        }
        if(!fl)
            System.out.println("-1");
	}
}
