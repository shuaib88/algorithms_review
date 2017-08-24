class BinaryTreeNode:

    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right


def is_bst(node):

    unvisited = []
    unvisited.append((node,-float('inf'),float('inf')))

    while unvisited:
        root,left_bound,right_bound = unvisited.pop()
        if not root:
            continue
        if (root.value >= right_bound) or (root.value <= left_bound):
            return False
        if root.right:
            unvisited.append((root.right, root.value, right_bound))
        if root.left:
            unvisited.append((root.left, left_bound, root.value))

    return True


def recursive_print(node):

    if node == None:
        return

    else:
        print(node.value)
        recursive_print(node.right)
        recursive_print(node.left)


root_node = BinaryTreeNode(20)
root_node.insert_left(10).insert_left(9)
root_node.left.insert_right(11)
root_node.insert_right(30).insert_left(25)
root_node.right.insert_right(31)

recursive_print(root_node)
is_bst(root_node)