# mine:(stupid)
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.main = set()
        self.pre = set()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        self.main.add(word)
        for i in range(1,len(word)+1):
            self.pre.add(word[:i])

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        return word in self.main

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        return prefix in self.pre


# # Your Trie object will be instantiated and called as such:
# # obj = Trie()
# # obj.insert(word)
# # param_2 = obj.search(word)
# # param_3 = obj.startsWith(prefix)



# updated:(Prefix Tree)
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        current = self.root
        for ch in word:
            if ch not in current:
                current[ch] = {}
            current = current[ch]
        current['#'] = 1
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        current = self.root
        for ch in word:
            if ch in current:
                current = current[ch]
            else:
                return False
        return '#' in current

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        current = self.root
        for ch in prefix:
            if ch in current:
                current = current[ch]
            else:
                return False
        return True

# # Your Trie object will be instantiated and called as such:
# # obj = Trie()
# # obj.insert(word)
# # param_2 = obj.search(word)
# # param_3 = obj.startsWith(prefix)

