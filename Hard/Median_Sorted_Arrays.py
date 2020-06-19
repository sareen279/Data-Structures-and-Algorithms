#Median of Two sorted arrays
#Given two sorted arrays arr1[] and arr2[] of sizes n and n2 respectively.
#The task is to find the median of the two arrays when they get merged.

arr1 = [1,2,3,4]
arr2 = [11,12,13,14]
n = len(arr1)
n2 = len(arr2)

if (n + n2) % 2 == 0:
    iseven = True
else:
    iseven = False
n3 = ((n + n2) // 2) + 1
i = 0
j = 0
k = 0
lt = []
while i < n and j < n2:
    if arr1[i] < arr2[j]:
        lt.append(arr1[i])
        i += 1
    else:
        lt.append(arr2[j])
        j += 1
    k += 1
while k < n3 and i < n:
    lt.append(arr1[i])
    i += 1
    k += 1
while k < n3 and j < n2:
    lt.append(arr2[j])
    j += 1
    k += 1
if iseven:
    print((lt[n3 - 1] + lt[n3 - 2]) // 2)
else:
    print(lt[n3 - 1])
