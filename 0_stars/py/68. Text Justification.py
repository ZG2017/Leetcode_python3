class Solution:
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        tmp = []
        total_len = 0
        where_the_blank = []
        res = []
        odd = 0
        all_words = words.copy()
        all_words.reverse()
        while all_words:
            i = all_words.pop()
            tmp.append(i)
            total_len += len(i)
            if total_len < maxWidth-1:
                tmp.append(" ")
                where_the_blank.append(len(tmp)-1)
                total_len += 1
                continue
            elif total_len == maxWidth:
                res.append("".join(tmp))
                tmp = []
                total_len = 0
                where_the_blank = []
                continue
            elif total_len == maxWidth -1:
                if len(where_the_blank) != 0:
                    tmp[where_the_blank[0]] += " "
                else:
                    tmp[0] += " "*(maxWidth-total_len)
                res.append("".join(tmp))
                tmp = []
                total_len = 0
                where_the_blank = []
                continue
            else:
                all_words.append(tmp.pop())
                tmp.pop()
                total_len -= len(i)+1
                where_the_blank.pop()
                odd = maxWidth - total_len
                if len(where_the_blank) != 0:
                    added_1 = odd//len(where_the_blank)
                    added_2 = odd%len(where_the_blank)
                    for j in range(len(where_the_blank)):
                        if j < added_2:
                            tmp[where_the_blank[j]] += " "*(added_1+1)
                        else:
                            tmp[where_the_blank[j]] += " "*added_1
                else:
                    tmp[0] += " "*(maxWidth-total_len)
                
                res.append("".join(tmp))
                tmp = []
                total_len = 0
                where_the_blank = []
                continue
        if tmp:
            tmp += [" "*(maxWidth-total_len)]
            res.append("".join(tmp))
        return res
