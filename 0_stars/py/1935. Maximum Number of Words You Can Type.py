class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        word_set_list = []
        for word in text.split(' '):
            word_set_list.append(set(word))
        ans = len(word_set_list)
        for cur_word_set in word_set_list:
            for broken_letter in brokenLetters:
                if broken_letter in cur_word_set:
                    ans -= 1
                    break
        return ans