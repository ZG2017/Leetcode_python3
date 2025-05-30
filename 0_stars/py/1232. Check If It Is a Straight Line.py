class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) <= 2:
            return True
        if coordinates[1][0] == coordinates[0][0]:
            for i in coordinates:
                if coordinates[0][0] != i[0]:
                    return False
        else:
            slope = (coordinates[1][1] - coordinates[0][1])/(coordinates[1][0] - coordinates[0][0])
            for i in range(2, len(coordinates)):
                if coordinates[i][0] - coordinates[0][0] == 0 or (coordinates[i][1] - coordinates[0][1])/(coordinates[i][0] - coordinates[0][0]) != slope:
                    return False
        return True



# better solution: to compare slope, we cand switch the base 


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x1,y1=coordinates[0][0],coordinates[0][1]
        x2,y2=coordinates[1][0],coordinates[1][1]
        for x3,y3 in coordinates[2:]:
            if (y3-y1)*(x2-x1)!=(x3-x1)*(y2-y1):
                return False
        else:
            return True
