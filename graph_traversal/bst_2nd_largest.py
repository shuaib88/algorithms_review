# Binary Searh Tree -- Top 2 items
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

def second_largest_element(root):

    if (not root.right) and (not root.left) or (not root.value):
        largest_element = "Not enough values in tree"
        return largest_element

    largest_element = -float('inf')
    second_largest = -float('inf')
    unvisited = []

    if root.right and root.left:
        largest_element = root.value
        unvisited.append(root.right)
    else:
        unvisited.append(root)

    while unvisited:

        current_node = unvisited.pop()
        print "current value: %s" % (current_node.value) if current_node else "current value: none"

        if current_node == None:
            continue

        if current_node.right:
            unvisited.append(current_node.right)
        if current_node.left:
            unvisited.append(current_node.left)

        if largest_element < current_node.value:
            second_largest = largest_element
            largest_element = current_node.value
            continue

        if second_largest < current_node.value:
            second_largest = current_node.value

        print "largest element: %s" % (largest_element)

    return second_largest

def largest_element(root):

    if not root.right:
        return root.value
    else:
        if root.right:
            return largest_element(root.right)
        else:
            return root.value

# iterative
def largest_element(root):
    current = root

    while current:
        if not current.right:
            return current.value
        else:
            current = current.right

# recursive considering all cases
def second_largest_element(root, parent=None):

    if root.right:
        return second_largest_element(root.right, root)
    else:
        # left exists -
        if root.left:
            if root.left.right:
                return root.left.right.value
            else:
                return root.left.value
        else:
            if not parent:
                return "less than 2 nodes"
            else:
                return parent.value
        # neither exist - return parent


# recursive simplest implementation, using largest element code
def second_largest_element(root, parent=None):

    if not root or (parent==None and (not root.right and not root.left)):
        raise Exception("not enough nodes")

    if not root.right and not root.left:
        return parent.value

    if root.right:
        return second_largest_element(root.right, root)
    else:
        return largest_element(root.left)

def second_largest_element(root, parent=None):

    current = root

    while current:
        # has right
        print ('one loop')

        if not root or (parent==None and (not current.right and not current.left)):
            raise Exception("not enough nodes")

        if not current.right and current.left:
            return largest_element(current.left)

        if not current.right and not current.left:
            return parent.value

        if current.right:
            parent = current
            current = current.right

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
# root_node.insert_right(30).insert_left(25)
# root_node.right.insert_right(31)


#recursive_print(root_node)
print largest_element(root_node.left)
print second_largest_element(root_node)


# notes
# when writing recursive function, the recursive call eventually evaluates and
# passes back to the original called function.. be sure to use keyword return when
# makeing recursive call --
#
#wrote out all the cases and then made sure the function covers all of them

