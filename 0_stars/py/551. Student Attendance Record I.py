class Solution:
    def checkRecord(self, s: str) -> bool:
        A_c = 0 
        for idx,i in enumerate(s):
            if i == "A":
                A_c += 1
                if A_c > 1:
                    return False
            elif i == "L":
                if s[idx:idx+3] == "LLL":
                    return False
        return True

