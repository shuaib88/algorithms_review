class Stack:

    # initialize an empty list
    def __init__(self):
        self.items = []

    # push a new item to the last index
    def push(self, item):
        self.items.append(item)

    # remove the last item
    def pop(self):
        # if the stack is empty, return None
        # (it would also be reasonable to throw an exception)
        if not self.items:
            return None
        return self.items.pop()

    # see what the last item is
    def peek(self):
        if not self.items:
            return None
        return self.items[-1]

class MaxStack(Stack):

    def __init__(self):
        Stack.__init__(self)
        self.largest = None
        self.largest_array = []

    def push(self,item):
        Stack.push(self,item)
        if item > self.largest:

            if self.largest:
               self.largest_array.append(self.largest)
            self.largest = item


    def pop(self):
        if self.items[-1] == self.largest:
            self.largest = self.largest_array.pop()
        Stack.pop(self)

    def get_max(self):
        if not self.largest:
            return IndexError('no items in stack')
        return self.largest




test = MaxStack()
test.push(3)
test.push(2)
test.push(4)
test.push(1)
test.push(1)
test.push(1)
test.pop()
test.pop()
test.pop()
test.pop()
test.push(9)
test.pop()
print test.get_max()