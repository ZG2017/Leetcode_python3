# hashmap

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        from collections import Counter
        overall_holder = Counter(words[0])
        for word in words:
            cur_holder = Counter(word)
            for char in overall_holder:
                if char in cur_holder:
                    overall_holder[char] = min(overall_holder[char], cur_holder[char])
                else:
                    overall_holder[char] = 0
        res = []
        return overall_holder.elements()
        # for char in overall_holder:
        #     if overall_holder[char] != 0:
        #         for _ in range(overall_holder[char]):
        #             res.append(char)
        # return res 