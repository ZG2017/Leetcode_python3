# mine:
class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        dit = {0:"A",1:"B",2:"C",3:"D",4:"E",5:"F",6:"G",7:"H",8:"I",\
               9:"J",10:"K",11:"L",12:"M",13:"N",14:"O",15:"P",16:"Q",17:"R",18:"S",\
              19:"T",20:"U",21:"V",22:"W",23:"X",24:"Y",25:"Z"}
        res = ""
        while n:
            res += dit[(n-1)%26]
            n = (n-1)//26
        return res[::-1]
