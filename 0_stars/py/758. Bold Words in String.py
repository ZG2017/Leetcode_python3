class Solution:
    def boldWords(self, words: List[str], S: str) -> str:
        tire = tire_tree()
        for word in words:
            tire.build(word)
        res_holder = []
        for index in range(len(S)):
            tmp = tire.check(S[index:])
            if tmp == -1:
                continue
            end = index + tmp
            if not res_holder:
                res_holder.append([index, end])
                continue
            else:
                if index <= res_holder[-1][1]+1:
                    if end <= res_holder[-1][1]:
                        continue
                    else:
                        cur_last = res_holder.pop()
                        cur_last[1] = end
                        res_holder.append(cur_last)
                elif index > res_holder[-1][1]:
                    res_holder.append([index, end])
        offset = 0
        for tmp in res_holder:
            real_begain = tmp[0] + offset
            real_end = tmp[1] + offset
            S = S[:real_begain] + "<b>" + S[real_begain:real_end+1] + "</b>" + S[real_end+1:]
            offset += 7
        return S
    
class tire_tree():
    def __init__(self):
        self.tree = {}

    def build(self, word):
        current = self.tree
        for char in word:
            if char not in current:
                current[char] = {}
            current = current[char]
                
        current[0] = None
    
    def check(self, string):
        current = self.tree
        holder = []
        for index, char in enumerate(string):
            if char in current:
                current = current[char]
                if 0 in current:
                    holder.append(index)
            else:
                if not holder:
                    return -1
                else:
                    return holder[-1]
        if holder:
            return holder[-1]
        else:
            return -1
