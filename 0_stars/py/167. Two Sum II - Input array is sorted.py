# mine:
class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        """
        for i in range(len(numbers)):
            tmp_t = target-numbers[i]
            if tmp_t in numbers[i+1:]:
                return [i+1,numbers[i+1:].index(tmp_t)+2+i]
        """
        p1 = 0
        p2 = len(numbers)-1
        while p1<p2:
            if numbers[p1]+numbers[p2] == target:
                return [p1+1,p2+1]
            elif numbers[p1]+numbers[p2] < target:
                p1 += 1
            else:
                p2 -= 1
        return None
