# 动态规划：
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        dp = [[0]*(m+1) for i in range(len(nums)+1)]
        holder = [0]
        tmp = 0
        for idx in range(1, len(nums)+1):
            tmp += nums[idx-1]
            dp[idx][1] = tmp
            holder.append(tmp)
        for i in range(1, len(nums)+1):
            for j in range(2, min(m, i)+1):
                tmp = []
                for k in range(1, i):
                    tmp.append(max(dp[k][j-1], holder[i]-holder[k]))
                dp[i][j] = min(tmp) if tmp else 0       
        return dp[len(nums)][m]


# 二分法：答案区间为（max(nums), sum(num)）,通过二分法找答案
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        # h = sum(nums)
        # l = max(nums)
        # while h>l:
        #     mid = int((h+l)/2)
        #     tmp = 0
        #     c = 1
        #     for i in nums:
        #         if tmp+i>mid:
        #             tmp=i
        #             c+=1
        #         else:
        #             tmp += i
        #     if c>m:
        #         l = mid+1
        #     else:
        #         h = mid
        # return l

