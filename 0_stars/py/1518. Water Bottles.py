class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = numBottles
        while numBottles >= numExchange:
            tmp = numBottles//numExchange
            numBottles = numBottles//numExchange + numBottles%numExchange
            res += tmp
        return res 