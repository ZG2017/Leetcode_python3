# 动态规划：dp[i]代表加i次油最大能跑到的里程。递推为dp[i+1] = dp[i] + (dp[i]里程内最大能加到的油量) 注意不要重复加油
# 其实也是一种贪心： 每次在能到的里程里，油料最多的加油站加油。
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        dp = [startFuel]+[0]*len(stations)
        fulled = set()
        for i in range(len(dp)-1):
            idx = 0
            while idx < len(stations) and stations[idx][0] <= dp[i]:
                idx += 1
            tmp = [(i[1], idx) for idx, i in enumerate(stations[:idx]) if idx not in fulled]
            if not tmp:
                dp[i+1] = -1
                break
            cur_max = max(tmp, key=lambda x: x[0])
            fulled.add(cur_max[1])
            dp[i+1] = dp[i] + cur_max[0]
        print(dp)
        for i in range(len(dp)):
            if dp[i] >= target:
                return i
        return -1
