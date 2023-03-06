
# class Node:

#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None


# def insert(root, node):

#     if root is None:
#         return node

#     if node.val < root.val:
#         root.left = insert(root.left, node)

#     elif node.val > root.val:
#         root.right = insert(root.right, node)

#     return root


# def printPreorder(root):

#     if root:

#         # then print the data of node
#         print(root.val)

#         # First recur on left child
#         printPreorder(root.left)

#         # now recur on right child
#         printPreorder(root.right)


