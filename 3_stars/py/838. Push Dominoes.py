# Time Limit Exceeded
class Solution(object):
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        if len(dominoes) <= 1:
            return dominoes

        pre_dp = list(dominoes)
        default = ['' for _ in range(len(dominoes))]
        cur_dp = default
        c = 1
        while c != 0:
            c = 0
            for idx in range(len(dominoes)):
                if pre_dp[idx] == '.':
                    if idx == 0:
                        if pre_dp[idx+1] == 'L':
                            c += 1
                            cur_dp[idx] = 'L'
                        else:
                            cur_dp[idx] = pre_dp[idx]
                    elif idx == len(dominoes) - 1:
                        if pre_dp[idx-1] == 'R':
                            c += 1
                            cur_dp[idx] = 'R'
                        else:
                            cur_dp[idx] = pre_dp[idx]
                    else:
                        if pre_dp[idx-1] == 'R' and pre_dp[idx+1] != 'L':
                            c += 1
                            cur_dp[idx] = 'R'
                        elif pre_dp[idx-1] != 'R' and pre_dp[idx+1] == 'L':
                            c += 1
                            cur_dp[idx] = 'L'
                        else:
                            cur_dp[idx] = pre_dp[idx]
                else:
                    cur_dp[idx] = pre_dp[idx]
            pre_dp = cur_dp[:]
            cur_dp = default[:]
        return ''.join(pre_dp)

# update: 
# 1. use two pointers to find the left and right of the dominoes
# 2. use two lists to store the left and right of the dominoes
# 3. compare the left and right of the dominoes
# 4. return the result

class Solution(object):
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        left_holder = []
        right_holder = []
        cur_idx, cur_s = 0, ''
        for idx, s in enumerate(dominoes):
            if idx == 0:
                cur_idx, cur_s = 0, dominoes[idx]
                left_holder.append((cur_idx, cur_s))
            else:
                if s == '.':
                    left_holder.append((cur_idx, cur_s))
                else:
                    left_holder.append((idx, s))
                    cur_idx, cur_s = idx, s
        cur_idx, cur_s = 0, ''
        for idx in range(len(dominoes)-1, -1, -1):
            s = dominoes[idx]
            if idx == len(dominoes)-1:
                cur_idx, cur_s = len(dominoes)-1, dominoes[idx]
                right_holder.append((cur_idx, cur_s))
            else:
                if s == '.':
                    right_holder.append((cur_idx, cur_s))
                else:
                    right_holder.append((idx, s))
                    cur_idx, cur_s = idx, s
        right_holder = right_holder[::-1]
        res = ''
        for idx in range(len(dominoes)):
            left, right = left_holder[idx], right_holder[idx]
            left_idx, left_s = left
            right_idx, right_s = right
            if dominoes[idx] == '.':
                if left_s == '.':
                    if right_s == 'L':
                        res += 'L'
                    else:
                        res += '.'
                elif right_s == '.':
                    if left_s == 'R':
                        res += 'R'
                    else:
                        res += '.'
                elif left_s == 'R' and right_s == 'L':
                    if idx - left_idx == right_idx - idx:
                        res += dominoes[idx]
                    elif idx - left_idx > right_idx - idx:
                        res += 'L'
                    else:
                        res += 'R'
                elif left_s == 'L' and right_s == 'L':
                    res += 'L'
                elif left_s == 'R' and right_s == 'R':
                    res += 'R'
                else:
                    res += dominoes[idx]
            else:
                res += dominoes[idx]
        return res
    
# update: https://leetcode.com/problems/push-dominoes/solutions/6706412/push-fall-the-ultimate-domino-chain-reaction/?envType=problem-list-v2&envId=dynamic-programming
# 1. use a list to store the force of the dominoes
# 2. use a variable to store the force of the dominoes
# 3. use a for loop to iterate through the dominoes
# 4. use a for loop to iterate through the dominoes in reverse
# 5. return the result

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        forces = [0] * n
        force = 0

        for i in range(n):
            if dominoes[i] == 'R':
                force = n
            elif dominoes[i] == 'L':
                force = 0
            else:
                force = max(force - 1, 0)
            forces[i] += force

        force = 0
        for i in range(n - 1, -1, -1):
            if dominoes[i] == 'L':
                force = n
            elif dominoes[i] == 'R':
                force = 0
            else:
                force = max(force - 1, 0)
            forces[i] -= force

        result = []
        for f in forces:
            if f == 0:
                result.append('.')
            elif f > 0:
                result.append('R')
            else:
                result.append('L')

        return ''.join(result)
