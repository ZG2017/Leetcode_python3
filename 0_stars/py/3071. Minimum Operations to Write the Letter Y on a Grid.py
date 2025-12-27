# cnt idx

class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        def get_y_coordinate(n):
            coordinates = set([])
            for i in range(n//2):
                coordinates.add((i,i))
                coordinates.add((i, n-1-i))
            for i in range((n//2), n):
                coordinates.add((i, (n//2)))
            return coordinates

        def get_y_cnt(n, y_coordinates):
            ans = {0:0, 1:0, 2:0}
            for i in range(n):
                for j in range(n):
                    if (i,j) in y_coordinates:
                        ans[grid[i][j]] += 1
            return ans
        
        def get_not_y_cnt(n, y_coordinates):
            ans = {0:0, 1:0, 2:0}
            for i in range(n):
                for j in range(n):
                    if (i,j) not in y_coordinates:
                        ans[grid[i][j]] += 1
            return ans
        
        def get_change_cnt(n_cnt):
            change_cnt = dict()
            change_cnt[0] = n_cnt[1] + n_cnt[2]
            change_cnt[1] = n_cnt[0] + n_cnt[2]
            change_cnt[2] = n_cnt[0] + n_cnt[1]
            return change_cnt

        def get_rest_n(n):
            if n == 0:
                return 1,2
            elif n == 1:
                return 0,2
            else:
                return 0,1

        n = len(grid)
        y_coordinates = get_y_coordinate(n)
        # print(y_coordinates)

        y_cnt = get_change_cnt(get_y_cnt(n, y_coordinates))
        not_y_cnt = get_change_cnt(get_not_y_cnt(n, y_coordinates))
        # print(y_cnt)
        # print(not_y_cnt)

        ans = min([y_cnt[i] + min(not_y_cnt[j] for j in get_rest_n(i)) for i in (0,1,2)])
        return ans

        