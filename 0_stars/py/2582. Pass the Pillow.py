class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        turns, remain = time//(n-1), time%(n-1)
        return 1+remain if turns%2==0 else n-remain 