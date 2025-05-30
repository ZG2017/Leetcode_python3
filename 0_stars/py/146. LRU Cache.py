# mine: take too much time
class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.queue = []
        self.dit = {}
        self.cap = capacity
        self.counter = 0

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.dit:
            self.queue.append(self.queue.pop(self.queue.index(key)))
            return self.dit[key]
        else:
            return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key not in self.dit:
            if self.counter < self.cap:
                self.dit[key] = value
                self.queue.append(key)
                self.counter += 1
            else:
                self.dit.pop(self.queue.pop(0))
                self.dit[key] = value
                self.queue.append(key)
        else:
            self.queue.append(self.queue.pop(self.queue.index(key)))
            self.dit[key] = value
                

# # Your LRUCache object will be instantiated and called as such:
# # obj = LRUCache(capacity)
# # param_1 = obj.get(key)
# # obj.put(key,value)


# updated: (using collections.OrderedDict to build a ordered hashmap)
class Node:
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.data = collections.OrderedDict()
        self.cap = capacity
    
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.data:
            self.data.move_to_end(key)
            return self.data[key]
        else:
            return -1
        
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.data:
            self.data.move_to_end(key)
        elif len(self.data) == self.cap:
            self.data.popitem(False)
        self.data[key] = value
