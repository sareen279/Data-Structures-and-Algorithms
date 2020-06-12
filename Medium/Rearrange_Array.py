#Rearrange an array with O(1) extra space
#Given an array arr[] of size N where every element is in the range from 0 to n-1.
#Rearrange the given array so that arr[i] becomes arr[arr[i]].
#Expected Time Complexity: O(N)
#Expected Auxiliary Space: O(1)

import math

def arrange(arr, n):
    #Main Logic
    for i in range(n):
        arr[i] += (arr[arr[i]] % n) * n
    for i in range(n):
        arr[i] //= n

def main():
        arr=[4,0,2,1,3]
        n = len(arr)
        arrange(arr,n)
        for i in arr:
            print(i,end=" ")
        print()

if __name__ == "__main__":
    main()
