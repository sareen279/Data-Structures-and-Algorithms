#Remove duplicate elements from sorted Array
#Given a sorted array A of size N. The function remove_duplicate takes two argu$
#n -> length of array, arr -> array
def remove_duplicate(n, arr):
    i = 0
    while(i < len(arr)-1):
        if arr[i] == arr[i+1]:
            arr.remove(arr[i])
        else:
            i+=1
    return len(arr)
