class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        for idx, i in enumerate(goal):
            if i == s[0]:
                if s == goal[idx:] + goal[:idx]:
                    return True
        return False 