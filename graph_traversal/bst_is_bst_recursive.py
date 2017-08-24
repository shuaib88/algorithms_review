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



# def is_bst(node):
#
#
#     if not node:
#         return
#
#     if (node.right):
#         if node.right.value <= node.value:
#             print "was false right"
#             return False
#         else:
#             is_bst(node.right)
#
#     if (node.left):
#         if node.left.value >= node.value:
#             print "was false left"
#             return False
#         else:
#             is_bst(node.left)

def is_bst(node):

    if not node:
        return True

    if node.right:
        if (node.right.value <= node.value):
            return False
    if node.left:
        if (node.left.value >= node.value):
            return False

    return is_bst(node.right) and is_bst(node.left)



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