class MyQueue(object):

    def __init__(self):
        self.st1 = []
        self.st2 = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        while self.st1:
            self.st2.append(self.st1.pop())
        self.st1.append(x)
        while self.st2:
            self.st1.append(self.st2.pop())
        
    def pop(self):
        """
        :rtype: int
        """
        if not self.st1:
            print('stack is empty')
            return -1
        else:
            top_element = self.st1.pop()
            return top_element

    def peek(self):
        """
        :rtype: int
        """
        if not self.st1:
            print('stack is empty')
            return -1
        return self.st1[-1]

        

    def empty(self):
        """
        :rtype: bool
        """
        if not self.st1:
            return True
        else:
            return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()