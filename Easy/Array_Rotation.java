//Rotate Array
//Given an unsorted array arr[] of size N, rotate it by D elements in the counter-clockwise direction.
//Expected Time Complexity - O(N)
//Expected Auxiliary Space - O(1)
//Algorithm used - Juggling Algorithm

import java.util.*;
import java.io.*;
import java.lang.*;

class Array_Rotation
{
    public static void main(String args[])
    {
        Array_Rotation ar = new Array_Rotation();
        int arr[] = {2 ,4, 6, 8, 10, 12, 14, 16, 18, 20};
        int d = 3;
        int n = arr.length;
        ar.rotateArr(arr, d, n);
        for(int i = 0;i < n;i++)
        {
            System.out.println(arr[i]);
        }
    }
    int gcd(int a, int b)
    {
        if(b == 0)
            return a;
        else
            return gcd(b, a%b);
    }
    void rotateArr(int arr[], int d, int n)
    {
        int g = gcd(d,n);
        System.out.println("g - " + g);
        int ct = 0;
        int i = 0;
        while(ct < g)
        {
            int j = i;
            int temp = arr[i];
            while(true)
            {
                int k = (j+d)%n;
                if(k == i)
                    break;
                arr[j] = arr[k];
                j = k;
            }
            arr[j] = temp;
            i+=1;
            ct++;
        }
    }
}
