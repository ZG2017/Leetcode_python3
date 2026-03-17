# every 2 negative numbers can turn to positive numbers following an arbitrary path from one negative number to the other.
# therefore, we can get final answer by considering the number of negative numbers and the number of positive numbers separately.

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        pos = []
        neg = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] > 0:
                    pos.append(matrix[i][j])
                else:
                    neg.append(matrix[i][j])

        # get answer given different number of negative and positive numbers.
        if len(neg) == 0:
            return sum(pos)
        elif len(pos) == 0:
            if len(neg)%2 == 0:
                return -sum(neg)
            else:
                biggest_neg = sorted(neg)[-1]
                return -sum(neg) + 2*biggest_neg
        else:
            if len(neg)%2 == 0:
                return sum(pos) - sum(neg)
            else:
                biggest_neg = sorted(neg)[-1]
                smallest_pos = sorted(pos)[0]
                if abs(biggest_neg) > abs(smallest_pos):
                    return -sum(neg) + sum(pos) - 2*smallest_pos
                else:
                    return -sum(neg) + sum(pos) + 2*biggest_neg
            
