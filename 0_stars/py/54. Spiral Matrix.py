# mine:
class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix == []:
            return []
        
        height = len(matrix)
        width = len(matrix[0])
        wall_dit = {0:width-1,1:height-1,2:0,3:1}
        # move_dit = {0:"going_right",1:"going_down",2:"going_left",3:"going_up"}
        move_pointer = 0
        ci_x = 0
        ci_y = 0
        res = []
        
        for _ in range(height*width):
            res.append(matrix[ci_x][ci_y])
            if move_pointer == 0:
                if ci_y < wall_dit[move_pointer]:
                    ci_y += 1
                else:
                    ci_x += 1
                    wall_dit[move_pointer] -= 1
                    move_pointer = (move_pointer+1)%4
            elif move_pointer == 1:
                if ci_x < wall_dit[move_pointer]:
                    ci_x += 1
                else:
                    ci_y -= 1
                    wall_dit[move_pointer] -= 1
                    move_pointer = (move_pointer+1)%4
            elif move_pointer == 2:
                if ci_y > wall_dit[move_pointer]:
                    ci_y -= 1
                else:
                    ci_x -= 1
                    wall_dit[move_pointer] += 1
                    move_pointer = (move_pointer+1)%4
            elif move_pointer == 3:
                if ci_x > wall_dit[move_pointer]:
                    ci_x -= 1
                else:
                    ci_y += 1
                    wall_dit[move_pointer] += 1
                    move_pointer = (move_pointer+1)%4
        return res
