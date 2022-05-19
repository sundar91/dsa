class node:

    def __init__(self, x):

        self.data = x
        self.left = None
        self.right = None

# A utility function to get the sum
# of values in tree with root as root


def sum(node):
    if node == None:
        return 0

    return node.data + sum(node.left) + sum(node.right)

# returns 1 if sum property holds
# for the given node and both of
# its children

# O(N^2)


def isLeaf(node):
    if node == None:
        return False

    if node.left == None and node.right == None:
        return True

    return False

# def isSumTree(node):
#     if node == None or (node.left == None and node.right == None):
#         return 1

#     ls = sum(node.left)
#     rs = sum(node.right)
#     if ls + rs == node.data and isSumTree(node.left) and isSumTree(node.right):
#         return 1

#     return 0

# O(N)


def isSumTree(node):
    if node == None:
        return 1
    if isLeaf(node):
        return 1

    if isSumTree(node.left) and isSumTree(node.right):

        if node.left == None:
            ls = 0
        elif isLeaf(node.left):
            ls = node.left.data
        else:
            ls = 2 * node.left.data

        if node.right == None:
            rs = 0
        elif isLeaf(node.right):
            rs = node.right.data
        else:
            rs = 2 * node.right.data

        return ls + rs == node.data

    return 0


# Driver code
if __name__ == '__main__':

    root = node(26)
    root.left = node(10)
    root.right = node(3)
    root.left.left = node(5)
    root.left.right = node(6)
    root.right.right = node(3)

    if(isSumTree(root)):
        print("The given tree is a SumTree ")
    else:
        print("The given tree is not a SumTree ")
