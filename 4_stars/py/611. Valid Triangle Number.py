# https://leetcode.com/problems/valid-triangle-number/solutions/7224465/simple-solution-beats-100-simple-trick-j-s405/

# given a,b,c as sides of a triangle, the triangle is valid if a + b > c when c is the longest side.
# 1. sort the array 
# 2. outer loop: iterate from biggest number to smallest number, and treat it as the longest side of the triangle.
# 3. inner loop: use two pointers to count the number of valid triangles.
# 4. since it's sorted, if nums[left] + nums[right] > nums[i], then nums[left+ 1...(right-1)] + nums[right] > nums[i] are also valid. So directly add right - left to count.

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        count = 0

        for i in range(n - 1, -1, -1):
            left, right = 0, i - 1
            while left < right:
                if nums[left] + nums[right] > nums[i]:
                    count += right - left
                    right -= 1
                else:
                    left += 1
        return count