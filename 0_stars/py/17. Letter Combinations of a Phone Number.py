class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dic = {2:["a","b","c"],
               3:["d","e","f"],
               4:["g","h","i"],
               5:["j","k","l"],
               6:["m","n","o"],
               7:["p","q","r","s"],
               8:["t","u","v"],
               9:["w","x","y","z"],}
        
        if digits == "":
            return []
        
        digits = list(digits)
        base = [""]
        for i in digits:
            base *= len(dic[int(i)])
            for index in range(len(base)):
                base[index]+=dic[int(i)][index//int(len(base)/len(dic[int(i)]))]
        return base
