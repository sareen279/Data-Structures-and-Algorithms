#Given a string s, task is to find the maximum occurring character in the string s.
#If more than one character occurs the maximum number of time then print the lexicographically smaller character.

s = 'sareenshah'
ct = 0
for i in s:
    curr = s.count(i)
    if curr > ct:
        let = i
        ct = curr
    elif curr == ct and i < let:
        let = i
print(let)
