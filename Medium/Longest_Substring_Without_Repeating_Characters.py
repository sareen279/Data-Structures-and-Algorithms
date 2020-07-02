#Longest Substring Without Repeating Characters
#Given a string S, find the length of its longest substring that does not have any repeating characters.
#Expected Time Complexity: O(N)
#Expected Space Complexity: O(1)

def SubsequenceLength(s):
    if len(s) == 0:
        return 0
    ss = s[0]
    ct = 1
    gct = 1
    for k in range(1,len(s)):
        if s[k] in ss:
            ss += s[k]
            ss = ss[ss.find(s[k])+1:]
            ct = len(ss)
        else:
            ct += 1
            ss += s[k]
        gct = max(gct,ct)
    return gct

s = 'geeksforgeeks'
print(SubsequenceLength(s))
