# hashmap

class SparseVector:
    def __init__(self, nums: List[int]):
        self.d = {i: x for i, x in enumerate(nums) if x}

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        dot_product = 0
        if len(self.d) <= len(vec.d):
            dot_product = sum(self.d[key]*vec.d.get(key, 0) for key in self.d)
        else:
            dot_product = sum(vec.d[key]*self.d.get(key, 0) for key in vec.d)

        return dot_product
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)