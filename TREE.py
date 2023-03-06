# TASK 1 PART (A)
import random
import time
import matplotlib.pyplot as plt


class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def insert(root, node):

    if root is None:
        return node

    if node.val < root.val:
        root.left = insert(root.left, node)

    elif node.val > root.val:
        root.right = insert(root.right, node)

    return root


def printPreorder(root):

    if root:

        # then print the data of node
        print(root.val)

        # First recur on left child
        printPreorder(root.left)

        # now recur on right child
        printPreorder(root.right)


def BFS(goal):
    explored = []
    q = []    # FIFO first in first out
    q.append(root)

    while len(q) > 0:
        node = q.pop(0)  # first out
        explored.append(node.val)

        if node.val == goal:
            print('Result:  ', explored)
            break

        if node.left is not None:
            q.append(node.left)

        if node.right is not None:
            q.append(node.right)


def DFS(goal):
    explored = []
    s = []    # stack (LAST IN FIRST OUT)
    s.append(root)

    while len(s) > 0:
        node = s.pop()
        explored.append(node.val)

        if node.val == goal:
            print('Result:  ', explored)
            break

        if node.right is not None:
            s.append(node.right)

        if node.left is not None:
            s.append(node.left)

# val = [10,5,3,7,15,12,17]

# root = Node(val[0])

# for i in val:
#     insert(root,Node(i))


# printPreorder(root)
# BFS(17)
# DFS(3)
val1 = []      # producing list of random 1000 numbers
for i in range(1000):
    v = random.randint(1, 900)
    val1.append(v)
val1 = list(set(val1))
root = Node(val1[0])
for i in val1:
    insert(root, Node(i))
n = len(val1)
start = time.time()
BFS(val1[n-1]-val1[120])
end = time.time()
thousand = end - start

val2 = []      # producing list of random 40000 numbers
for i in range(40000):
    v = random.randint(1, 900)
    val2.append(v)
val = list(set(val2))
root = Node(val2[0])
for i in val2:
    insert(root, Node(i))
start = time.time()
BFS(val2[899]-val2[120])
end = time.time()
forty_k = end - start

val3 = []      # producing list of random 80000 numbers
for i in range(80000):
    v = random.randint(1, 900)
    val3.append(v)
val3 = list(set(val3))
root = Node(val3[0])
for i in val3:
    insert(root, Node(i))
start = time.time()
BFS(val3[899]-val3[120])
end = time.time()
eighty_k = end - start

val4 = []      # producing list of random 200000 numbers
for i in range(200000):
    v = random.randint(1, 900)
    val4.append(v)
val4 = list(set(val4))
root = Node(val4[0])
for i in val4:
    insert(root, Node(i))
start = time.time()
BFS(val4[899]-val4[120])
end = time.time()
twohundred_k = end - start


val = []      # producing list of random 1000000 numbers
for i in range(1000000):
    v = random.randint(1, 900)
    val.append(v)

val = list(set(val))

root = Node(val[0])   # setting root node as the very first element of list

for i in val:
    insert(root, Node(i))    # inserting each element into the tree

# print (len(val))

# printPreorder(root)   # traversing the BST

start = time.time()
BFS(val[899]-val[120])
end = time.time()
million = end - start
# print("TIME TAKEN: ",end - start)
# DFS(val[611]-val[120])

yplot = [len(val1), len(val2), len(val3), len(val4), len(val1)]
xplot = [thousand, forty_k, eighty_k, twohundred_k, million]


plt.bar(xplot, yplot, color='r', width=0.4)
plt.show()
