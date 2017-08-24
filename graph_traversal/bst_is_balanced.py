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

def is_balanced(tree_root):

    # tree with no nodes
    if tree_root == None:
        return True

    depths = []
    nodes = []
    nodes.append((tree_root,0))

    while len(nodes):
        node, depth = nodes.pop()
        print(depths)
        if (not node.left) and (not node.right):
            if depth not in depths:
                depths.append(depth)

                if len(depths) == 2:
                    if abs(depths[0]-depths[1]) > 1:
                        return False

                if len(depths) > 2:
                    return False
        if node.left:
            nodes.append((node.left, depth+1))

        if node.right:
            nodes.append((node.right, depth+1))


    if len(depths) == 1:
        return False

    return True

# test
node1 = BinaryTreeNode(1)

node1.insert_right(2)
node1.insert_left(2)
node1.left.insert_right(3)
node1.left.insert_left(4)
node1.left.left.insert_left(3)

# execution
print is_balanced(node1)
