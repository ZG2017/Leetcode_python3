class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        holder = dict([(5, 0), (10, 0), (20, 0)])
        for bill in bills:
            change = bill - 5
            if change == 0:
                holder[5] += 1
                continue
            else:
                while change:
                    if change > 10:
                        if holder[10] > 0:
                            holder[10] -= 1
                            change -= 10
                        elif holder[5] > 0:
                            holder[5] -= 1
                            change -= 5
                        else:
                            return False
                    else:
                        if holder[5] > 0:
                            holder[5] -= 1
                            change -= 5
                        else:
                            return False
                holder[bill] += 1
        return True
                


