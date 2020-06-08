#Leaders in an array
#Given an array A of positive integers. Your task is to find the leaders in the array.
#An element of array is leader if it is greater than or equal to all the elements to its right side. Also, the rightmost element is always a leader.

A = [16,17,4,3,5,2]
A.reverse()
lt = [A[0]]
for i in range(1,len(A)):
    if A[i] >= lt[len(lt)-1]:
        lt.append(A[i])
lt.reverse()
print(lt)
