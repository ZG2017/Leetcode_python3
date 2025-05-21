class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) <= 0 or len(matrix[0]) <= 0:
            return 0
        rows = set()
        cols = set()
        num_row = len(matrix)
        num_col = len(matrix[0])
        
        for i_row in range(num_row):
            rows.add(min(matrix[i_row]))
            
        for i_col in range(num_col):
            holder = []
            for i_row in range(num_row):
                holder.append(matrix[i_row][i_col])
            cols.add(max(holder))
        
        return rows&cols
