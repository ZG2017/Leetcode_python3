class Solution:
    def find_position(self, num):
        p1 = 0
        p2 = len(self.holder)-1
        while p2 >= p1:
            mid = (p2+p1)//2
            if num < self.holder[mid]:
                p2 = mid-1
            else:
                p1 = mid+1
        return p1

    def nextGreaterElement(self, nums1, nums2):
        if len(nums2) == 1:
            return [-1]
        elif len(nums2) == 0:
            return []
        self.holder = [nums2[0]]
        res = dict()
        for i in nums2[1:]:
            pos = self.find_position(i)
            for j in self.holder[:pos]:
                res[j] = i
            self.holder = [i] + self.holder[pos:]
        output = []
        for i in nums1:
            if i in res:
                output.append(res[i])
            else:
                output.append(-1)
        return output


# update solution: stack
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ng = defaultdict(lambda: -1)
        st = []

        for num in nums2:
            while st and st[-1] < num:
                ng[st.pop()] = num
            st.append(num)
        
        return [ng[num] for num in nums1]
