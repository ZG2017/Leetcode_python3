# mine:
class Solution:
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        saver = []	
        tmp = (1,n)
        flag = True    # True for left, and False for right 
        while tmp != (0,0) and tmp != (1,1):
            if flag == True:
                if (tmp[1]-tmp[0]+1)%2 == 0:
                    if tmp[0] == 1:
                        tmp = (1,int(tmp[1]/2))
                        saver.append(0)
                    else:
                        tmp = (0,int(tmp[1]/2))
                        saver.append(1)
                else:
                    if tmp[0] == 1:
                        tmp = (1,int(tmp[1]/2))
                        saver.append(0)
                    else:
                        tmp = (0,int((tmp[1]-1)/2))
                        saver.append(1)
                flag = False
            else:
                if (tmp[1]-tmp[0]+1)%2 == 0:
                    if tmp[0] == 0:
                        saver.append(0)
                    else:
                        saver.append(1)
                    tmp = (0,int((tmp[1]-1)/2))
                else:
                    if tmp[0] == 0:
                        tmp = (0,int((tmp[1]-1)/2))
                        saver.append(1)
                    else:
                        tmp = (1,int((tmp[1]-1)/2))
                        saver.append(0)
                flag = True
        res = tmp[0]
        for i in reversed(saver):
            res = res*2+i
        return res
