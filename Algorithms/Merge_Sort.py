#Merge_Sort
#Contains 2 functions - MergeSort and Merge
#Time Complexity - O(NlogN)

def merge(arr, l, m, r):
    ar1 = arr[l:m+1]
    ar2 = arr[m+1:r+1]
    i = 0
    j = 0
    n1 = len(ar1)
    n2 = len(ar2)
    k = l
    while i < n1 and j < n2:
        if ar1[i] < ar2[j]:
            arr[k] = ar1[i]
            i+=1
        else:
            arr[k] = ar2[j]
            j+=1
        k+=1
    while i < n1:
        arr[k] = ar1[i]
        i+=1
        k+=1
    while j < n2:
        arr[k] = ar2[j]
        j+=1
        k+=1

def mergeSort (arr, l, r):
    if l < r:
        m = l + (r - l)//2
        mergeSort (arr, l, m)
        mergeSort (arr, m+1, r)
        merge (arr, l, m, r)

if __name__ == "__main__":
    arr = [10,5,2,7,4,8,1]
    n = len(arr)
    mergeSort(arr, 0, n-1)
    for i in range(n):
        print(arr[i],end=" ")
    print()
