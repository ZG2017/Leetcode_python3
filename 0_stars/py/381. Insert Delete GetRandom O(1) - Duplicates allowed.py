# mine: (not excally o(1),but accepted)
class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.saver = {}
        self.list = []
        self.tmp = 0

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.saver:
            self.saver[val] = []
            self.saver[val].append(len(self.list))
            self.list.append(val)
            return True
        else:
            self.saver[val].append(len(self.list))
            self.list.append(val)
            return False

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.saver:
            index = self.saver[val].pop()
            if index != len(self.list)-1:
                self.list[index],self.list[-1] = self.list[-1],self.list[index]
                if self.saver[self.list[index]]: 
                    self.saver[self.list[index]][-1] = index
                    self.saver[self.list[index]].sort()
            self.list.pop()
            if not self.saver[val]: self.saver.pop(val)
            return True
        return False
        

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        import random
        if self.list:
            return random.choice(self.list)
        else:
            return None
        


# # Your RandomizedCollection object will be instantiated and called as such:
# # obj = RandomizedCollection()
# # param_1 = obj.insert(val)
# # param_2 = obj.remove(val)
# # param_3 = obj.getRandom()
