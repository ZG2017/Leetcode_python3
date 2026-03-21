# https://leetcode.com/problems/minimum-number-of-operations-to-make-all-array-elements-equal-to-1/solutions/7342559/solution-of-the-day-9967-beats-all-in-on-s0w3/

# the key is to find the first 1 in the array.
# if there is already 1s in the array, we can make all the other elements equal to 1 with one operation each. the number of operations is n - number of 1s.
# if there is no 1s in the array, we need to find the shortest subarray with a gcd equal to 1.
# we can use a greedy approach to find the shortest subarray with a gcd equal to 1. 
# Note thet gcd(a,b,c) = gcd(gcd(a,b),c) = gcd(a,gcd(b,c)), where we can do the linear scan to find the shortest subarray with a gcd equal to 1.

class Solution:
    def gcd(self, a, b):
        if a > b:
            bigger = a
            smaller = b
        else:
            bigger = b
            smaller = a
        if bigger%smaller == 0:
            return smaller
        else:
            return gcd(smaller, bigger%smaller)


    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        # check if there is 1 in `nums`
        ones = nums.count(1)
        # if so, we can make all the other elements equal to 1 with one operation each
        # e.g. [2,6,1,4] -> [2,1,1,4] -> [1,1,1,4] -> [1,1,1,1]
        # the number of operation to make all equal to 1 is simply n - number of 1s
        if ones: return n - ones
        res = float('inf')
        # try finding the shortest subarray with a gcd equal to 1.
        for i in range(n):
            # subarray starting from i
            g = nums[i]
            # try each element after i
            for j in range(i + 1, n):
                # to calculate gcd
                g = self.gcd(g, nums[j])
                # if the gcd is 1
                if g == 1:
                    # then we calculate the min ops
                    res = min(res, j - i)
        
        if res == float('inf'): 
            # no result -> return -1
            return -1
        else:
            # otherwise, return res + n - 1
            # i.e. the min ops to turn the shortest subarray to 1 + 
            #      use that 1 to convert n - 1 elements to 1
            return res + n - 1
        