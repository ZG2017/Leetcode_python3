# mine:
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.hl = []
        self.hh = []
        self.mid = []
        self.lens = 0
    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        from heapq import heappush
        from heapq import heappop
        if self.lens == 0:
            self.mid.append(num)
        elif self.lens == 1:
            if num > self.mid[0]:
                self.mid.append(num)
            else:
                self.mid = [num] + self.mid
        elif self.lens%2 == 0:
            if num <= self.mid[0]:
                heappush(self.hl,(-num,num))
                tmp = self.mid.pop(1)
                heappush(self.hh,tmp)
            elif num > self.mid[0] and num < self.mid[1]:
                heappush(self.hl,(-self.mid[0],self.mid[0]))
                heappush(self.hh,self.mid[1])
                self.mid = [num]
            elif num >= self.mid[1]:
                heappush(self.hh,num)
                tmp = self.mid.pop(0)
                heappush(self.hl,(-tmp,tmp))
        elif self.lens%2 == 1:
            if num < self.hl[0][1]:
                self.mid = [heappop(self.hl)[1]] + self.mid
                heappush(self.hl,(-num,num))
            elif num <= self.mid[0] and num >= self.hl[0][1]:
                self.mid = [num] + self.mid
            elif num > self.mid[0] and num <= self.hh[0]:
                self.mid.append(num)
            elif num > self.hh[0]:
                self.mid.append(heappop(self.hh))
                heappush(self.hh,num)
        self.lens += 1
    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.mid) == 1:
            return float(self.mid[0])
        else:
            return sum(self.mid)/2


# # Your MedianFinder object will be instantiated and called as such:
# # obj = MedianFinder()
# # obj.addNum(num)
# # param_2 = obj.findMedian()
