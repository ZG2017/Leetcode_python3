class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        sorted_words = sorted(words, key=lambda x:len(x), reverse=True)
        res = 0
        self.prefix_tree = dict()
        for word in sorted_words:
            if not self.checkPrefix(word):
                self.buildPrefixTree(word)
                res += len(word)+1
        return res
            
    def buildPrefixTree(self, word):
        cur_prefix_tree = self.prefix_tree
        for i in word[::-1]:
            if i not in cur_prefix_tree:
                cur_prefix_tree[i] = dict()
            cur_prefix_tree = cur_prefix_tree[i]
        cur_prefix_tree['\t'] = 0
    
    def checkPrefix(self, word):
        cur_prefix_tree = self.prefix_tree
        for i in word[::-1]:
            if i in cur_prefix_tree:
                cur_prefix_tree = cur_prefix_tree[i]
            else:
                return False
        return True
        
