# updated:
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0
        p1 = 0
        p2 = len(citations)-1
        tmp = len(citations)
        res = 0
        while p2 >= p1:
            index = int((p1+p2)/2)
            if index - 1 >= 0 and citations[index - 1] > tmp - index:
                p2 = index-1
            elif citations[index] < tmp - index:
                p1 = index+1
            elif citations[index] >= tmp - index:
                if index - 1 < 0 or index - 1 >= 0 and citations[index-1] <= tmp - index:
                    res = tmp - index
                    break
        return res
