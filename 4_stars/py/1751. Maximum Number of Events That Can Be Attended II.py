# knapsack problem variant

# TLE solution: linear search for the last non-overlapping event

class Solution:
    def build_prev_dict(self, events):
        holder = []
        for idx, (start, end, _) in enumerate(events, 1):
            holder.append((start, 1, idx))
            holder.append((end, 0, idx))
        holder.sort(key=lambda x: x[0])
        prev_dict = dict()
        for holder_idx, (time, tag, idx) in enumerate(holder):            
            if tag == 1: # end time
                cur_holder_idx = holder_idx
                while cur_holder_idx >= 0:
                    cur_time, cur_tag, cur_idx = holder[cur_holder_idx]
                    if cur_tag == 0 and cur_time != time:
                        prev_dict[idx] = cur_idx
                        break
                    else:
                        cur_holder_idx -= 1
                if idx not in prev_dict:
                    prev_dict[idx] = 0
        return prev_dict

    def maxValue(self, events: List[List[int]], k: int) -> int:
        # Step 1: Sort events by end time
        events.sort(key=lambda x: x[1])
        n = len(events)

        # build_prev_dict
        prev_dict = self.build_prev_dict(events)
        print(prev_dict)

        # Step 2: Extract start times separately for binary search
        start_times = [e[0] for e in events]

        # Step 3: Initialize DP table
        dp = [[0] * (k+1) for _ in range(n+1)]

        # Step 4: Loop through each event
        for i in range(1, n+1):
            start, end, value = events[i-1]

            # Step 5: Binary search for last non-overlapping event

            prev = prev_dict[i]

            for j in range(1, k+1):
                # Option 1: skip current event
                # Option 2: take current event and add to prev best
                dp[i][j] = max(dp[i-1][j], dp[prev][j - 1] + value)
        
        print(dp)

        # Step 6: Return final answer
        return dp[n][k]


# update solution: binary search for the last non-overlapping event
# https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended-ii/solutions/6933226/easy-solution-eng-hing-explained-beats-9-14a4/

class Solution:
    def maxValue(self, events, k):
        # Step 1: Sort events by end time
        events.sort(key=lambda x: x[1])
        n = len(events)

        # Step 2: Extract start times separately for binary search
        start_times = [e[0] for e in events]

        # Step 3: Initialize DP table
        dp = [[0] * (k + 1) for _ in range(n + 1)]

        # Step 4: Loop through each event
        for i in range(1, n + 1):
            start, end, value = events[i - 1]

            # Step 5: Binary search for last non-overlapping event
            prev = self.findLastNonOverlapping(events, i - 1, start)

            for j in range(1, k + 1):
                # Option 1: skip current event
                # Option 2: take current event and add to prev best
                dp[i][j] = max(dp[i - 1][j], dp[prev + 1][j - 1] + value)

        # Step 6: Return final answer
        return dp[n][k]

    def findLastNonOverlapping(self, events, right, targetStart):
        left = 0
        res = -1
        while left <= right:
            mid = (left + right) // 2
            if events[mid][1] < targetStart:
                res = mid
                left = mid + 1
            else:
                right = mid - 1
        return res