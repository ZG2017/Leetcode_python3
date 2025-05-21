# mine:(TLE)
class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        if endWord not in wordList:
            return []
        n = len(beginWord)
        res = {}
        dit = dict(zip(wordList,[[] for _ in range(len(wordList))]))
        for word1 in wordList:
            for word2 in wordList:
                if word1 == word2:
                        continue
                for i in range(len(word1)):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        if word1[:i]+c+word1[i+1:] == word2:
                            dit[word1].append(word2)
        dit[beginWord] = []
        for word2 in wordList:
            if word2 == beginWord:
                continue
            for i in range(len(word1)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    if beginWord[:i]+c+beginWord[i+1:] == word2:
                        dit[beginWord].append(word2)
        print(dit)
        def helper(current_begin,tmp):
            if current_begin == endWord:
                m = len(tmp)
                if m not in res:
                    res[m] = []
                res[m].append(tmp)
                return
            for word in dit[current_begin]:
                if word in tmp:
                    continue
                helper(word,tmp+[word])
        helper(beginWord,[beginWord])
        if res:
            return res[min(res)]
        else:
            return []


# updated:

