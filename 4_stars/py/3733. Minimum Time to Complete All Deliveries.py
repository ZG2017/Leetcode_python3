# https://leetcode.com/problems/minimum-time-to-complete-all-deliveries/solutions/7319829/binary-search-on-answers-by-vedantmehta1-bayj/
# find a actual patten is hard, but evaluation given a time is easier, so we use binary search to find the minimum time
# slots1: the number of times drone 1 can deliver
# slots2: the number of times drone 2 can deliver
# total_slots: the number of times the system can deliver   (accounting for shared recharge times)      
# finally, binary search to find the minimum time

class Solution:
    def minimumTime(self, d: List[int], r: List[int]) -> int:
        # Define the binary search range for the total time T.
        # low: Minimum possible time (no recharges)
        # high: A sufficiently large upper bound
        low = d[0] + d[1]
        high = 2 * (low) * 2 
        ans = high

        # Pre-calculate the LCM of the recharge intervals.
        # lcm(a, b) = (a * b) / gcd(a, b)
        lcm = (r[0] * r[1]) // math.gcd(r[0], r[1])

        def can_complete(time):
            """
            Checks if all deliveries can be completed within 'time'
            by verifying all three capacity conditions.
            """
            # 1. Check Drone 1 capacity
            slots1 = time - (time // r[0])
            
            # 2. Check Drone 2 capacity
            slots2 = time - (time // r[1])
            
            # 3. Check total system capacity (accounting for shared recharge times)
            total_slots = time - (time // lcm)
            
            return (slots1 >= d[0]) and (slots2 >= d[1]) and (total_slots >= d[0] + d[1])

        # Binary search for the minimum time
        while low <= high:
            mid = (low + high) // 2
            if can_complete(mid):
                ans = mid       # This time works, try to find a smaller one
                high = mid - 1
            else:
                low = mid + 1   # This time doesn't work, need more time
        
        return ans