# modified from: https://leetcode.com/problems/time-needed-to-rearrange-a-binary-string/solutions/2454195/python3-on-dp-approach-by-ye15-t16l/

class Solution: 
    def secondsToRemoveOccurrences(self, s: str) -> int:
        ans = 0 # answer of moving current 1 to the left
        c_zeros = 0 # num of zeros before current i
        for i, ch in enumerate(s): 
            if ch == '1':
                if c_zeros != 0: 
                    # there are 0s before this 1, we need to move current 1
                    # num of moves is max between (steps of moving previous 1 plus 1) and number of 0s before it.
                    ans = max(ans+1, c_zeros)
                else: # there is no 0s before this 1, no need to move current 1 (ans==0)
                    ans = 0
            else: # num of 0s plus 1
                c_zeros += 1
        return ans 