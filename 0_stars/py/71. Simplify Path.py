# mine: (not good)
class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        res = []
        tmp = []
        path += "/"
        for i in path:
            if i == "/":
                if not tmp:
                    tmp += [i]
                else:
                    tmp = "".join(tmp)
                    if tmp == "/.":
                        tmp = ["/"]
                    elif tmp == "/..":
                        if res:
                            res.pop()
                        tmp = ["/"]
                    elif tmp == "/":
                        tmp = list(tmp)
                    else:
                        res += [tmp]
                        tmp = ["/"]
            else: 
                tmp += [i]
        if not res:
            return "".join(tmp)
        return "".join(res)


# updated:
class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        
        parts = path.split('/')
        # use stack
        
        valid_parts = []    
        for part in parts:
            if part == '' or part == '.':
                pass
            elif part == '..':
                if len(valid_parts) > 0:
                    valid_parts.pop()
            else:
                valid_parts.append(part)
        return '/' + '/'.join(valid_parts)
