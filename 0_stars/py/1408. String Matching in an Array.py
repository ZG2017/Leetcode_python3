# brute force with sort
class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        sorted_words = sorted(words, key=lambda x: len(x), reverse=True)
        in_ans = [False] * len(words)
        ans = []
        for i in range(len(sorted_words)-1):
            for j in range(i+1, len(sorted_words)):
                if in_ans[j]:
                    continue
                if sorted_words[j] in sorted_words[i]:
                    ans.append(sorted_words[j])
                    in_ans[j] = True
        return ans
    
# brute force without sort (faster)
class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        result = []
        n = len(words)
        for i in range(n):
            for j in range(n):
                if i != j and words[i] in words[j]:
                    result.append(words[i])
                    break
        return result