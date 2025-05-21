# Check each number's remainder. if 2 numbers' remainder add up to k, it means the add-up of 2 numbers is also divisible by k.

# refer: https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/solutions/5854122/100-beats-easy-to-understand-step-by-step-explaination-beginner-friendly/

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        freq = [0] * k

        for num in arr:
            remainder = (num % k + k) % k
            freq[remainder] += 1

        if freq[0] % 2 != 0:
            return False

        for i in range(1, k // 2 + 1):
            if freq[i] != freq[k - i]:
                return False

        return True


