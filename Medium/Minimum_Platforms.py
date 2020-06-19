#Minimum Platforms
#Given arrival and departure times of all trains that reach a railway station.
#Your task is to find the minimum number of platforms required for the railway station so that no train waits.
#Note - same platform can not be used for both departure of a train and arrival of another.
#Expected Time Complexity: O(nLogn)
#Expected Auxiliary Space: O(n)

arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]
n = len(arr)
curr = 0
mx = 0
arr.sort()
dep.sort()
i = 0
j = 0
while i < n:
    if arr[i] <= dep[j]:
        curr += 1
        if curr > mx:
            mx = curr
        i += 1
    else:
        curr -= 1
        j += 1
print(mx)
