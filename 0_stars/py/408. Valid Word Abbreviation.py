# re style solution:

class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        import re
        p1 = 0 
        p2 = 0
        abbrs = []
        while p2 != len(abbr):
            if abbr[p2] in '1234567890':
                cur_number = [abbr[p2]]
                p2 += 1
                while p2 != len(abbr) and abbr[p2] in '1234567890':
                    cur_number.append(abbr[p2])
                    p2 += 1
                cur_number = ''.join(cur_number)
                if cur_number.startswith('0'):
                    return False
                abbrs.append(int(cur_number))
            else:
                abbrs.append(str(abbr[p2]))
                p2 += 1
        pattern = '^' + ''.join([i if isinstance(i, str) else r'\w{%d}'%(i) for i in abbrs]) + '$'

        res = re.match(pattern, word)
        if res:
            return True
        else:
            return False

# two pointers solution:

class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        p1 = 0 
        p2 = 0
        while p2 != len(abbr) and p1 != len(word):
            if abbr[p2] in '1234567890':
                cur_number = [abbr[p2]]
                p2 += 1
                while p2 != len(abbr) and abbr[p2] in '1234567890':
                    cur_number.append(abbr[p2])
                    p2 += 1
                cur_number = ''.join(cur_number)
                if cur_number.startswith('0'):
                    return False
                cur_number = int(cur_number)
                p1 += cur_number
                if p1 > len(word):
                    return False
            else:
                if word[p1] != abbr[p2]:
                    return False
                else:
                    p1 += 1
                    p2 += 1
        if p1 != len(word) or p2 != len(abbr):
            return False
        else:
            return True