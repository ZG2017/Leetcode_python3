class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        res = 0
        sum_energy = sum(energy)
        res += max(sum_energy-initialEnergy+1, 0)
        
        cur_experience = initialExperience
        for i in experience:
            if i >= cur_experience:
                res += i-cur_experience+1
                cur_experience += i-cur_experience+1
            cur_experience += i
        return res

