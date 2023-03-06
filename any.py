from anytree import Node
from anytree import RenderTree
from anytree.exporter import DotExporter

root = Node(50)
Node (43, parent = root)
Node (55, parent = root)
Node (40, parent = root.children[0])
Node (45, parent = root.children[0])
Node (53, parent = root.children[1])
Node (60, parent = root.children[1])
Node (38, parent= root.children[0].children[0])
Node (41, parent= root.children[0].children[0])
Node (44, parent= root.children[0].children[1])
Node (47, parent= root.children[0].children[1])
Node (52, parent= root.children[1].children[0])
Node (54, parent= root.children[1].children[0])
Node (59, parent= root.children[1].children[1])
Node (68, parent= root.children[1].children[1])

# Print the tree structure using RenderTree
for pre, fill, node in RenderTree(root):
    print(f"{pre}{node.name}")

# DotExporter(50).to_picture("udo.png")