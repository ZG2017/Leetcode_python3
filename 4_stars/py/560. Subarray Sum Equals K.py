# prefix sum (TLE)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if len(nums) == 0:
            return 0
        res = 0
        cur_sum = 0
        prefix_sum = [0]
        for i in nums:
            cur_sum += i
            prefix_sum.append(cur_sum)
        for i in range(len(nums)+1):
            for j in range(i+1,len(nums)+1):
                if prefix_sum[j]-prefix_sum[i] == k:
                    res += 1
        return res


# prefix sum + hashmap
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        holder_dict = {0:1}
        tmp = 0
        counter = 0
        for i in nums:
            tmp += i
            if tmp-k in holder_dict:
                counter += holder_dict[tmp-k]
            holder_dict[tmp] = holder_dict.get(tmp, 0) + 1
        return counter
        
