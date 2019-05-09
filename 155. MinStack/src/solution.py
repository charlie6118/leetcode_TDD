class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.min_v = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.data.append(x)
        if len(self.min_v) == 0:
            self.min_v.append(x)
        else:
            if self.min_v[-1] >= x:
                self.min_v.append(x)
        

    def pop(self):
        """
        :rtype: None
        """
        if self.top() == self.min_v[-1]:
            self.min_v.pop()
        
        return self.data.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.data[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_v[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()