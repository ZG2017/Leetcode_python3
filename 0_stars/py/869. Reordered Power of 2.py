# hashmap

class Solution:
    def __init__(self):
        self.holder = [1]
        i = 1
        while i <= 10**9:
            i *= 2
            self.holder.append(i)
        self.digit_holder = dict()
        for i in self.holder:
            self.digit_holder[''.join(sorted(str(i)))] = i
        
    def reorderedPowerOf2(self, n: int) -> bool:
        if ''.join(sorted(str(n))) in self.digit_holder:
            return True
        else:
            return False
