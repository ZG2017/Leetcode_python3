class Solution:
    def find_numbers(self, num1, num2):
        cur = num1
        next = num2
        count = 0
        while cur<=self.n:
            count += min(next, self.n+1) - cur
            cur *= 10
            next *= 10
        return count

    def findKthNumber(self, n: int, k: int) -> int:
        # return sorted([str(i) for i in range(1, n+1)])[k-1]
        self.n = n
        total_count = 0
        cur = 1
        next = cur + 1
        while cur<n:
            current_count = self.find_numbers(cur, next)
            if current_count + total_count < k:
                total_count += current_count
                cur += 1
                next = cur + 1
            elif current_count + total_count >= k:
                total_count += 1
                if total_count == k:
                    break
                else:
                    cur *= 10
                    next = cur + 1
        return cur

            
            


        
