from typing import List

class Solution:
    def countSeniors(self, details: List[str]) -> int:
        return len([True for i in details if int(i[-4:-2]) > 60]) 