#Union of Two Sorted Arrays
#Given two sorted arrays arr[] and brr[] of size N and M respectively. The task is to find the union of these two arrays.
#Union of two arrays can be defined as the common and distinct elements in the two arrays.
#Expected Time Complexity: O(N+M)
#Expected Auxiliary Space: O(N+M)

def mergeArrays(a,b,n,m):
    lt = []
    i = 0
    j = 0
    if a[n - 1] > b[m - 1]:
        ct = [0] * (a[n - 1] + 1)
    else:
        ct = [0] * (b[m - 1] + 1)
    while i < n and j < m:
        if a[i] < b[j]:
            if ct[a[i]] == 0:
                lt.append(a[i])
                ct[a[i]] = 1
            i+=1
        elif b[j] < a[i]:
            if ct[b[j]] == 0:
                lt.append(b[j])
                ct[b[j]] = 1
            j+=1
        else:
            if ct[b[j]] == 0:
                lt.append(b[j])
                ct[b[j]] = 1
            i+=1
            j+=1
    while i < n:
        if ct[a[i]] == 0:
            lt.append(a[i])
            ct[a[i]] = 1
        i+=1
    while j < m:
        if ct[b[j]] == 0:
            lt.append(b[j])
            ct[b[j]] = 1
        j+=1
    return lt

a = [1,2,3,4,4]
n = len(a)
b = [1,2,2,2,2,2,5]
m = len(b)
print(mergeArrays(a,b,n,m))
