class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        holder = {"0":"qwertyuiop", "1":"asdfghjkl", "2":"zxcvbnm"}
        reversed_holder = dict()
        for i in holder:
            for j in holder[i]:
                reversed_holder[j] = i
        res = []
        for word in words:
            tmp = word.lower()
            if len(set([reversed_holder[i] for i in tmp])) == 1:
                res.append(word)
        return res

