#Who has the majority?
#You are given an array arr[] of size N. You are also given two elements x and y. Now, you need to tell which element (x or y) appears most in the array.
#In other words, return the element, x or y, that has higher frequency in the array.
#If both elements have the same frequency, then just return the smaller element.

arr = [1,2,3,4,5,6,7,8]
x = 7
y = 1
xcount = arr.count(x)
ycount = arr.count(y)
print(x if xcount > ycount else y if ycount > xcount else x if x < y else y)
