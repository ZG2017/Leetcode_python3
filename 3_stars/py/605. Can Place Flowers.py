if-else + concern cases

class Solution:
    import math
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        s = -1
        res = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 1:
                if s == -1:
                    res += math.ceil((i-1)/2)
                else:
                    if i-s-3 > 0:
                        res += math.ceil((i-s-3)/2)
                s = i
        if flowerbed[-1] == 0:
            if s == -1:
                res += math.ceil(len(flowerbed)/2)
            else:
                res += math.ceil((len(flowerbed)-s-2)/2)
        return res >= n
