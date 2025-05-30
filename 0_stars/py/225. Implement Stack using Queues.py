# mine:
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        import queue
        self.q = queue.Queue()
        self.lens = 0
        

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.q.put(x)
        self.lens += 1

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        for i in range(self.lens-1):
            self.q.put(self.q.get())
        self.lens -= 1
        return self.q.get()

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        for i in range(self.lens-1):
            self.q.put(self.q.get())
        tmp = self.q.get()
        self.q.put(tmp)
        return tmp

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return self.lens == 0


# # Your MyStack object will be instantiated and called as such:
# # obj = MyStack()
# # obj.push(x)
# # param_2 = obj.pop()
# # param_3 = obj.top()
# # param_4 = obj.empty()
