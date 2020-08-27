# https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.inbox = []
        self.outbox = []

    def push(self, x):
        """
        Push element x to the back of queue.
        """
        self.inbox.append(x)
    
    def shuffle(self):
        while len(self.inbox) > 0:
            self.outbox.append(self.inbox.pop())
        

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        """
        if len(self.outbox) == 0:
            self.shuffle()
        return self.outbox.pop()
        

    def peek(self):
        """
        Get the front element.
        """
        if len(self.outbox) == 0:
            self.shuffle()
        if len(self.outbox) > 0:
            return self.outbox[-1]
        else:
            return None
        

    def empty(self):
        """
        Returns whether the queue is empty.
        """
        return (len(self.inbox) == 0 and len(self.outbox) == 0)
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()