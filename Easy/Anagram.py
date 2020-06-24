#Given two strings a and b consisting of lowercase characters.
#The task is to check whether two given strings are an anagram of each other or not.
#Expected Time Complexity: O(N)

def isAnagram(a,b):
    if len(a) != len(b):
        return False
    a = sorted(a)
    b = sorted(b)
    for (i,j) in zip(a,b):
        if i != j:
            return False
    return True

a = 'actt'
b = 'tacc'

if isAnagram(a,b):
    print('They are anagrams')
else:
    print('Not anagrams')
