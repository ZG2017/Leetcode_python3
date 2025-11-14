# backtracking with pruning

class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        holder = [0] * k
        self.ans = float('inf')

        def helper(rounds):
            if len(cookies) == rounds:
                self.ans = min(self.ans, max(holder))
                return
            for i in range(k):
                if holder[i] + cookies[rounds] >= self.ans:
                    continue
                holder[i] += cookies[rounds]
                helper(rounds + 1)
                holder[i] -= cookies[rounds]
        helper(0)
        return self.ans

# dp with bitmask
# https://leetcode.com/problems/fair-distribution-of-cookies/solutions/3702322/w-explanationcpython-with-recursive-dp-b-6dwh/

class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        n = len(cookies)
        dp = [[-1] * (1 << n) for _ in range(k + 1)]
        
        def unfairness(k, bagMask):
            if dp[k][bagMask] != -1: 
                return dp[k][bagMask]
            
            def sum_cookies(Mask):
                sum=0
                for i in range(n):
                    if Mask&(1<<i):
                        sum+=cookies[i]
                return sum
            # end of  sum_cookies 
            if k==1:
                dp[k][bagMask] = sum_cookies(bagMask)
                return dp[k][bagMask]
            ans=2**31
            Mask=bagMask
            while(Mask>0):
                sum1=sum_cookies(Mask)
                sum2=unfairness(k - 1, bagMask ^ Mask)
                ans=min(ans, max(sum1, sum2))
                Mask=(Mask - 1) & bagMask
            dp[k][bagMask] = ans
            return ans
        # end of unfairness
        return unfairness(k, (1 << n) - 1)
