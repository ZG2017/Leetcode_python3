class Solution:
    def originalDigits(self, s: str) -> str:
        flags = ("w","g","u","z","h","f","o","v","s","i")
        self.info = dict([(flag, 0) for flag in flags])
        self.holder = dict([(i,0) for i in range(10)])
        for i in self.info:
            self.info[i] = s.count(i)
        
        self.holder[2] = self.info["w"]
        self.holder[8] = self.info["g"]
        self.holder[4] = self.info["u"]
        self.holder[0] = self.info["z"]
        self.holder[3] = self.info["h"] - self.holder[8]
        self.holder[5] = self.info["f"] - self.holder[4]
        self.holder[1] = self.info["o"] - self.holder[0] - self.holder[2] - self.holder[4]
        self.holder[7] = self.info["v"] - self.holder[5] 
        self.holder[6] = self.info["s"] - self.holder[7]
        self.holder[9] = self.info["i"] - self.holder[5] - self.holder[6] - self.holder[8]
        
        res = []
        for i in self.holder:
            for j in range(self.holder[i]):
                res.append(str(i))
        return "".join(sorted(res))

