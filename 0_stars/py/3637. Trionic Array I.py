class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        if nums[0] > nums[1]:
            return False
        increase = True
        n_turn = 0
        
        for idx in range(len(nums)-1):
            if n_turn > 2:
                return False
            
            if increase:
                if nums[idx+1] > nums[idx]:
                    continue
                elif nums[idx+1] == nums[idx]:
                    return False
                else:
                    n_turn += 1
                    if n_turn > 2:
                        return False
                    increase = not increase
            else:
                if nums[idx+1] < nums[idx]:
                    continue
                elif nums[idx+1] == nums[idx]:
                    return False
                else:
                    n_turn += 1
                    if n_turn > 2:
                        return False
                    increase = not increase
        if n_turn != 2:
            return False
        else:
            return True