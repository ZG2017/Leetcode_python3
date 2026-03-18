# dp: dp[i] means the best energy we can get at the index i. 
# trans: dp[i] = max(energy[i], dp[i-k] + energy[i])
# at each index i, the best energy we can get is the maximum between energy[i] and energy[i-k] plus energy[i].

class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        if len(energy) <= k:
            return max(energy)
        ans = -float('inf')
        best_energy = [0]*len(energy)
        for idx in range(len(energy)):
            if idx - k >= 0:
                best_energy[idx] = max(energy[idx], best_energy[idx - k] + energy[idx])
            else:
                best_energy[idx] = energy[idx]
            if idx + k > len(energy) - 1:
                ans = max(ans, best_energy[idx])
        return ans
                

        
        