class Solution:
    import random
    def __init__(self, nums: List[int]):
        self.holder = dict()
        for idx, item in enumerate(nums):
            if item not in self.holder:
                self.holder[item] = []
            self.holder[item].append(idx)


    def pick(self, target: int) -> int:
        return random.choice(self.holder[target])


# # Your Solution object will be instantiated and called as such:
# # obj = Solution(nums)
# # param_1 = obj.pick(target)
