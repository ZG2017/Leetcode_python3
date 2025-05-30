# mine:
class MyCalendarTwo:

    def __init__(self):
        self.dit = {}
        self.saver = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        if not self.saver:
            self.saver.append(start)
            self.saver.append(end)
            self.dit[start] = 1
            self.dit[end] = 0
            return True
        else:
            import bisect
            index_s = bisect.bisect_left(self.saver,start)
            if index_s >= len(self.saver):
                self.saver = self.saver+[start,end]
                self.dit[start] = 1
                self.dit[end] = 0
                return True
            index_e = bisect.bisect_right(self.saver,end)
            if index_e <= 0:
                self.saver = [start,end] + self.saver
                self.dit[start] = 1
                self.dit[end] = 0
                return True
            tmp_dit = self.dit.copy()
            tmp_saver = self.saver.copy()
            p1 = index_s
            if index_s == index_e:
                self.saver.insert(index_s,start)
                self.saver.insert(index_e+1,end)
                self.dit[start] = self.dit[self.saver[index_s-1]]+1
                self.dit[end] = self.dit[self.saver[index_s-1]]
                if self.dit[start] >= 3 or self.dit[end] >= 3:
                    self.dit = tmp_dit.copy()
                    self.saver = tmp_saver.copy()
                    return False
                return True
            while p1<index_e-1:
                self.dit[self.saver[p1]] += 1
                if self.dit[self.saver[p1]] >= 3:
                    self.dit = tmp_dit.copy()
                    self.saver = tmp_saver.copy()
                    return False
                p1 += 1
            flag = False
            if self.saver[index_s] != start:
                flag = True
                self.saver.insert(index_s,start)
                self.dit[start] = self.dit[self.saver[index_s-1]] + 1
                if self.dit[start] >= 3:
                    self.dit = tmp_dit.copy()
                    self.saver = tmp_saver.copy()
                    return False
            if flag:
                index_e = index_e+1
            if self.saver[index_e-1] != end:
                self.dit[self.saver[index_e-1]] += 1
                if self.dit[self.saver[index_e-1]] >= 3:
                    self.dit = tmp_dit.copy()
                    self.saver = tmp_saver.copy()
                    return False
                self.saver.insert(index_e,end)
                self.dit[end] = self.dit[self.saver[index_e-1]] - 1
            return True

# # Your MyCalendarTwo object will be instantiated and called as such:
# # obj = MyCalendarTwo()
# # param_1 = obj.book(start,end)



# updated: (only record overlap to decide if triple booked happend)
class MyCalendarTwo:

    def __init__(self):
        self.booked = []
        self.overlap = []
        
    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        for i, j in self.overlap:
            if start < j and end > i:
                return False
        
        for i, j in self.booked:
            if start < j and end > i:
                self.overlap.append((max(i, start), min(j, end)))
        self.booked.append((start, end))
        return True
