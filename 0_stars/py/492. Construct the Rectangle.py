class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        max_ = int(area**0.5)
        for i in reversed(range(1,max_+1)):
            if area%i == 0:
                return [area//i, i]
        return [area, 1]
