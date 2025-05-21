if one char's in_degree == 0, then we can append this char to the result str since there is no more precursor.

class Solution:
    def check_part(self, str1, str2):
        i = 0
        while i < len(str1) and i < len(str2):
            if str1[i] == str2[i]:
                i += 1
                continue
            if (str2[i], str1[i]) in self.ok_holder:
                return False
            else:
                self.ok_holder.add((str1[i], str2[i]))
                return True
        if len(str1) > len(str2):
            return False
        else:
            return True

    def build(self):
        res = []
        queue = []
        for i in self.in_degree:
            if self.in_degree[i] == 0:
                queue.append(i)
        while queue:
            cur = queue.pop(0)
            res.append(cur)
            if cur in self.link_holder:
                for i in self.link_holder[cur]:
                    self.in_degree[i] -= 1
                    if self.in_degree[i] == 0:
                        queue.append(i)
        if len(res) == len(self.vocab):
            return ''.join(res)
        else:
            return ''

    def alienOrder(self, words: List[str]) -> str:
        self.ok_holder = set([])
        self.vocab = set([])

        for i in range(len(words)-1):
            for j in range(i+1, len(words)):
                self.vocab = self.vocab.union(set(list(words[i])))
                cur_res = self.check_part(words[i], words[j])
                if not cur_res:
                    return ""

        self.vocab = self.vocab.union(set(list(words[-1])))
        if len(self.vocab) == 1:
            return ''.join(list(self.vocab))
        self.n = len(self.vocab)
        self.link_holder = dict()
        self.in_degree = dict([(i, 0) for i in self.vocab])
        for i,j in self.ok_holder:
            if i not in self.link_holder:
                self.link_holder[i] = []
            self.link_holder[i].append(j)
            self.in_degree[j] += 1
        return self.build()

