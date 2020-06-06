#Remove duplicate elements from sorted Array
#Given a sorted array A of size N. The function remove_duplicate takes two arguments . The first argument is the sorted array A[ ] and the second argument is 'N' the size of the array and returns the size of the new converted array A[ ] with no duplicate element.
#n -> length of array, arr -> array
#Example:
#Input:
#2
#5
#2 2 2 2 2
#3
#1 2 2
#Output:
#2
#1 2
def remove_duplicate(n, arr):
    i = 0
    while(i < len(arr)-1):
        if arr[i] == arr[i+1]:
            arr.remove(arr[i])
        else:
            i+=1
    return len(arr)
