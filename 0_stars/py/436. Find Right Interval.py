class Solution:
    def bin_search(self, tar, start_idx):
        p1 = start_idx
        p2 = self.len_ - 1
        while p2 >= p1:
            mid = (p2+p1)//2
            if self.sorted_holder[mid][0] >= tar:
                p2 = mid-1
            else:
                p1 = mid+1
        if p1 != start_idx and p1 < self.len_:
            return p1
        else:
            return None

    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        holder = dict([(tuple(item), idx) for idx,item in enumerate(intervals)])
        self.len_ = len(intervals)
        self.sorted_holder = sorted(intervals, key=lambda x:x[0])
        res = [-1 for i in range(self.len_)]
        for idx in range(self.len_):
            tar = self.sorted_holder[idx][1]
            final_idx = self.bin_search(tar, idx)
            if final_idx:
                res[holder[tuple(self.sorted_holder[idx])]] = holder[tuple(self.sorted_holder[final_idx])]
        return res
