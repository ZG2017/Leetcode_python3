# MLE solution: devide and conquer

class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        if len(target) == 0:
            return 0
        if len(target) == 1:
            return target[0]

        # get minimum value and idx
        cur_min = float('inf')
        for v in target:
            if v < cur_min:
                cur_min = v
        min_idx = []
        for idx, v in enumerate(target):
            if v == cur_min:
                min_idx.append(idx)
        min_idx.append(len(target))
        
        # compute each segment and cumulate the results
        pre_idx = 0
        ans = cur_min
        for i in min_idx:
            cur_target = target[pre_idx:i]
            real_cur_target = []
            for j in cur_target:
                real_cur_target.append(j-cur_min)
            ans += self.minNumberOperations(real_cur_target)
            pre_idx = i+1
        return ans


# update solution
# https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array/solutions/7312095/beats-99-explained-by-karanagnani-8a5i/
# if next > prev, next-prev more operations are needed to reach the next value.
# if next <= prev, no operation is needed since we can reached with previous operations.

class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        res = prev = 0
        for x in target:
            if x > prev:
                res += x - prev
            prev = x
        return res