# TLE
class Solution(object):
    def is_subset(self, w1, w2):
        for c, c_c in w2.items():
            if c not in w1 or w1[c] < c_c:
                return False
        return True

    def wordSubsets(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: List[str]
        """
        from collections import Counter
        holder_1 = dict()
        for i, word in enumerate(words1):
            holder_1[i] = Counter(word)
        holder_2 = dict()
        for i, word in enumerate(words2):
            holder_2[i] = Counter(word)

        overall_holder = dict()
        for i in range(len(words2)):
            overall_holder[i] = set([])
            for j in range(len(words1)):
                if self.is_subset(holder_1[j], holder_2[i]):
                    overall_holder[i].add(j)
    
        ans = overall_holder[0]
        # print(ans)
        for i in range(1, len(words2)):
            ans = ans.intersection(overall_holder[i])
            # print(ans)
        return list([words1[i] for i in ans])


# updated: only check the maximum count of each character in words2 to determine if the word in words1 is a subset
class Solution(object):
    def wordSubsets(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: List[str]
        """
        from collections import Counter
        
        req = Counter()
        for word in words2:
            cur = Counter(word)
            for ch in cur:
                req[ch] = max(req[ch], cur[ch])
        
        ans = []
        for word in words1:
            cur = Counter(word)
            if all(cur[ch] >= req[ch] for ch in req):
                ans.append(word)
        
        return ans
