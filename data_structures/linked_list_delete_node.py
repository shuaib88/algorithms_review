class LinkedListNode:

    def __init__(self, value):
        self.value = value
        self.next  = None


def delete_node(node_to_delete):
    next_value = node_to_delete.next.value
    node_to_delete.value = next_value
    if node_to_delete.next:
        node_to_circumvent = node_to_delete.next
        if node_to_circumvent.next:
            node_to_delete.next = node_to_circumvent.next
            node_to_circumvent.next = None



a = LinkedListNode('A')
b = LinkedListNode('B')
c = LinkedListNode('C')

a.next = b
b.next = c

delete_node(b)


