class LinkedListNode:

    def __init__(self, value):
        self.value = value
        self.next  = None


def does_contain_cycle(node):
    visited = []
    visited.append(node)
    visited_dict = {}
    current_node = node
    while current_node.next:
        print (current_node.value)
        if current_node in visited_dict:
            return True
        else:
            if current_node.next:
                visited_dict[current_node] = None
    return False

# Analysis
# Space is O(n), Time is O(n)

def does_contain_cycle(node):

    current_node = node
    while current_node:
        if current_node.value == "visited":
            return True
        else:
            current_node.value = "visited"
            current_node = current_node.next

    return False

# space O(1), Time is O(n), but destroys the list

def does_contain_cycle(node):

    slow_runner = node
    fast_runner = node

    while fast_runner is not None and fast_runner.next is not None:
        slow_runner = slow_runner.next
        fast_runner = fast_runner.next.next
        
        if fast_runner == slow_runner:
            return True
    return False




a = LinkedListNode('A')
b = LinkedListNode('B')
c = LinkedListNode('C')
d = LinkedListNode('D')
e = LinkedListNode('E')
f = LinkedListNode('F')

a.next = b
b.next = c
c.next = d
d.next = e


i = 0
def print_nodes(node, i):
    while i < 4:
        print node.value
        i += 1
        print_nodes(node.next, i)

# print_nodes(a,i)

print does_contain_cycle(a)