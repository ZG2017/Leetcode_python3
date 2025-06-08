class Solution(object):
    def getLongestSubsequence(self, words, groups):
        """
        :type words: List[str]
        :type groups: List[int]
        :rtype: List[str]
        """
        result = []
        last = -1
        for i in range(len(words)):
            if groups[i] != last:
                result.append(words[i])
                last = groups[i]
        return result