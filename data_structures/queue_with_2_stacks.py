class Queue:

    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    #O(m)
    def enqueue(self,element):
        self.in_stack.append(element)


    def dequeue(self):
        if not self.out_stack:
            while self.in_stack:
                newest_item = self.in_stack.pop()
                self.out_stack.append(newest_item)
            if not self.out_stack:
                raise IndexError('queue is empty')

        return self.out_stack.pop()

#test
test_queue = Queue()
test_queue.enqueue(1)
test_queue.enqueue(2)
test_queue.enqueue(3)
test_queue.enqueue(4)


print test_queue.in_stack, test_queue.out_stack
dequeued = test_queue.dequeue()
dequeued = test_queue.dequeue()
dequeued = test_queue.dequeue()
dequeued = test_queue.dequeue()
print dequeued, test_queue.in_stack, test_queue.out_stack




