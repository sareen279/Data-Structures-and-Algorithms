#Intersection of two sorted arrays
#Given two sorted arrays arr1[] and arr2[] of sizes N and M respectively.
#The task is to find intersection of the two arrays.
#Intersection of two arrays contains the elements common to both the arrays
#The intersection should not count duplicate elements.
#Expected Time Complexity: O(N + M)
#Expected Auxiliary Space: O(N + M)

a = [1,2,3,4]
b = [2,4,6,7,8]
n = len(a)
m = len(b)
lt = []
if a[n - 1] > b[m - 1]:
    ct = [0] * (a[n - 1] + 1)
else:
    ct = [0] * (b[m - 1] + 1)
for i in a:
    if ct[i] == 0:
        ct[i] = 1
for i in b:
    if ct[i] == 1:
        lt.append(i)
        ct[i] += 1
if len(lt) == 0:
    lt.append(-1)
print(lt)
