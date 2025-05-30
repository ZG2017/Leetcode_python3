# greedy + 2 pointers

class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        if len(tokens) <= 0:
            return 0
        tokens.sort()
        h_p, t_p = 0, len(tokens)-1

        if power < tokens[h_p]:
            return 0
        max_s = 0
        cur_s = 0
        cur_power = power
        while h_p <= t_p:
            if cur_power >= tokens[h_p]:
                cur_s += 1
                cur_power -= tokens[h_p]
                h_p += 1
                max_s = max(max_s, cur_s)
            else:
                if cur_s > 0 and cur_power + tokens[t_p] >= tokens[h_p]:
                        cur_s -= 1
                        cur_power += tokens[t_p]
                        t_p -= 1
                else:
                    break
        return max_s

