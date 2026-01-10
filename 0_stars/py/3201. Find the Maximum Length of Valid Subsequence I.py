# there are 4 cases:
# 1. all even numbers
# 2. all odd numbers
# 3. alternating even and odd numbers
# 4. alternating odd and even numbers
# so we need to count the number of all even numbers and all odd numbers, and the number of alternating even and odd numbers and alternating odd and even numbers.
# the answer is the maximum of the number of all even numbers and all odd numbers, and the number of alternating even and odd numbers and alternating odd and even numbers.

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        is_e_tags = [True if num %2 == 0 else False for num in nums]

        o_c = 0
        e_c = 0
        for num in is_e_tags:
            if num:
                e_c += 1
            else:
                o_c += 1
        
        # even-odd
        eo_flag = True # True means we looking for even number right now, False mean odd
        eo_c = 0
        oe_flag = False
        oe_c = 0
        for num, real_num in zip(is_e_tags, nums):
            if eo_flag:
                if num:
                    eo_c += 1
                    eo_flag = not eo_flag
            else:
                if not num:
                    eo_c += 1
                    eo_flag = not eo_flag

            if oe_flag:
                if num:
                    oe_c += 1
                    oe_flag = not oe_flag
            else:
                if not num:
                    oe_c += 1
                    oe_flag = not oe_flag
        return max(o_c, e_c, oe_c, eo_c)

                