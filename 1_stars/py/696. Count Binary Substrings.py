# first, segment the string into groups of consecutive characters
# then, for each group, the number of valid substrings is the minimum of the number of consecutive characters in the group

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        count = 1 
        arr = []
        for i in range(1,len(s)) :
            if s[i] == s[i-1] :
                count += 1
            else :
                arr.append(count) 
                count = 1
        arr.append(count)
        count = 0
        for i in range(1,len(arr)) :
            count += min(arr[i],arr[i-1])
        return count