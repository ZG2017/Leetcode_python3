class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        p_holder = [0 for i in range(len(mat))]
        small_holder = [tmp[0] for tmp in mat]
        if len(set(small_holder)) == 1:
            return small_holder[0]
        while len(set(small_holder)) != 1:
            smallest = min(small_holder)
            for index, i in enumerate(small_holder):
                if mat[index][p_holder[index]] == smallest:
                    p_holder[index] += 1
                    if p_holder[index] >= len(mat[0]):
                        return -1
                    small_holder[index] = mat[index][p_holder[index]]
        return small_holder[0]
        
        
