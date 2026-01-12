class Solution:
    def isValid(self, word: str) -> bool:
        vowel = dict([(i, True) for i in 'aeiouAEIOU'])
        c = len(word)
        if c < 3:
            return False
        contain_vowel = False
        contain_consonant = False
        for c in word:
            if ord('A') <= ord(c) <= ord('Z') or ord('a') <= ord(c) <= ord('z') or ord('0') <= ord(c) <= ord('9'):
                if not (ord('0') <= ord(c) <= ord('9')):
                    if c in vowel:
                        contain_vowel = True
                    else:
                        contain_consonant = True
            else:
                return False
        if contain_vowel and contain_consonant:
            return True
        else:
            return False
