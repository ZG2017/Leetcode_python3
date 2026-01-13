# 2 pointer solution

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        if len(fruits) <= 2:
            return len(fruits)
        max_ans = 0
        p1, p2 = 0, 0
        cur_ans = 0
        fruit_holder = dict()
        while p2 < len(fruits):
            if fruits[p2] not in fruit_holder:
                if len(fruit_holder) == 2:
                    while p1 <= p2 and len(fruit_holder) == 2:
                        if fruit_holder[fruits[p1]] >= 2:
                            fruit_holder[fruits[p1]] -= 1
                        elif fruit_holder[fruits[p1]] == 1:
                            fruit_holder.pop(fruits[p1])
                        p1 += 1
                        cur_ans -= 1
                fruit_holder[fruits[p2]] = 1
                cur_ans += 1
                max_ans = max(max_ans, cur_ans)
            else:
                fruit_holder[fruits[p2]] = fruit_holder.get(fruits[p2], 0) + 1
                cur_ans += 1
                max_ans = max(max_ans, cur_ans)
            p2 += 1
            # print(fruit_holder)
            # print(max_ans)
            # print('---------')
        return max_ans

        