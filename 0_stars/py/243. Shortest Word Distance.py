class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        min_dis = float('inf')
        index1 = -1
        index2 = -1
        for i in range(len(wordsDict)):
            if wordsDict[i]==word1:
                index1 = i
            if wordsDict[i]==word2:
                index2 = i
            if index1!=-1 and index2!=-1:
                min_dis = min(min_dis, abs(index2-index1))
        return min_dis
        
                