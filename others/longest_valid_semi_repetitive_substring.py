"""
## Question

You are given a digit string s that consists of digits from 0 to 9. 

A string is called semi-repetitive if there is at most one adjacent pair of the same digit. 
For example, "0010", "002020", "0123", "2002", and "54944" are semi-repetitive,
while the following are not: 
    - "00101022" (adjacent same digit pairs are 00 and 22), 
    - "1101234883" (adjacent same digit pairs are 11 and 88).

Return the length of the longest semi-repetitive substring of s. 

## Examples

Input: s = "52233" 
Output: 4 
Explanation: 
    The longest semi-repetitive substring is "5223". Picking the whole string "52233" has two adjacent same digit pairs 22 and 33, but at most one is allowed. 

Input: s = "54944" 
Output: 5
Explanation: 
    s is a semi-repetitive string. 

Input: s = "1111111" 
Output: 2 
Explanation: 
    The longest semi-repetitive substring is "11". Picking the substring "111" has two adjacent same digit pairs, but at most one is allowed. 

## Constraints
1 <= s.length <= 50 
'0' <= s[i] <= '9'
"""


# p1: start of valid substring
# p2: previous index of adjacent pair of the same digit
def solver(string):
    p1, p2 = 0, 0
    ans = 1
    counter = 0
    i = 0
    for i in range(1, len(string)):
        if string[i-1] == string[i]: # adjacent pair of the same digit  
            if counter == 0: # never encounter adjacent pair of the same digit before
                counter += 1
                p2 = i
            else: # has encountered adjacent pair of the same digit before
                p1 = p2
                p2 = i
        ans = max(ans, i-p1+1)
    return ans