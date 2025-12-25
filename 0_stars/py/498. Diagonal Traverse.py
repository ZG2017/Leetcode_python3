class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        hashmap={}

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if i+j not in hashmap:
                    hashmap[i+j]=[]
                hashmap[i+j].append(mat[i][j])
        ans=[]
        for i in range(len(hashmap)):
            if i%2==0:
                ans.extend((hashmap[i])[::-1])
            else:
                ans.extend(hashmap[i])
        return ans
