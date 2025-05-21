# updated:(TLE)
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        cur_level = [beginWord]
        next_level = []
        depth = 1
        n = len(beginWord)
        while cur_level:
            for item in cur_level:
                if item == endWord:
                    return depth
                for i in range(n):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        word = item[:i] + c + item[i + 1:]
                        if word in wordList:
                            wordList.remove(word)
                            next_level.append(word)
            depth += 1
            cur_level = next_level
            next_level = []
        return 0

# updated:(TLE, use queue, dfs)
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        q = [(beginWord,1)]
        while q:
            e,lens = q.pop(0)
            if e == endWord: return lens
            for i in range(len(e)):
                left = e[:i]
                right = e[i + 1:]
                for c in 'abcdefghigklmnopqrstuvwxyz':
                    if e[i] != c:
                        nextWord = left + c + right
                        if nextWord in wordList:
                            q.append((nextWord,lens + 1))
                            wordList.remove(nextWord)
        return 0
