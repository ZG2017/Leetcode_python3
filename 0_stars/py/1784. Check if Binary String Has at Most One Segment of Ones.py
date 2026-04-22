class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        seg_s = s.split('0')
        flag = False
        for i in seg_s:
            if '1' in i:
                if flag:
                    return False
                else:
                    flag = True
        return flag

