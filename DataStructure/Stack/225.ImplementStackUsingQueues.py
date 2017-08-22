"""
Implement the following operations of a stack using queues.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.
Notes:
You must use only standard operations of a queue -- which means only "push to back",
"peek/pop from front", "size", and "is empty" operations are valid.
Depending on your language, queue may not be supported natively. You may simulate a queue
by using a list or dequeue (double-ended queue), as long as you use only standard operations
of a queue.
You may assume that all operations are valid(for example, no pop or top operations will be called on
an empty stack)
--------------------------------Approach---------------------------------------------
1.In computer science, peek is an operation on certain abstract data types, specifically sequential
collections such as stacks and queues, which returns the value of the top ("front") of the
collection without removing the element from the collection.

2.
Queue first in first out --- the top is the first --->queue[0]
Stack first in last out  --- the top is the last -----> stack[-1]

3.Both Queue and Stack append the last element in the tail -----> see push
"""
class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []


    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.queue.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        for i in range(len(self.queue)-1):
            self.queue.append(self.queue.pop(0))
        return self.queue.pop(0)
    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        top = None
        for i in range(len(self.queque)):
            top  = self.queue.pop(0)
            self.queue.append(top)
        return top

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return self.queue == []


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
