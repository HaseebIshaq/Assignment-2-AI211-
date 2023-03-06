from treelib import Tree

# Create the tree and add nodes
tree = Tree()
tree.create_node(50, "a")  # root node
tree.create_node(43, "b", parent="a")
tree.create_node(55, "c", parent="a")
tree.create_node(40, "d", parent="b")
tree.create_node(45, "e", parent="b")
tree.create_node(53, "f", parent="c")
tree.create_node(60, "g", parent="c")
tree.create_node(38, "h", parent="d")
tree.create_node(41, "i", parent="d")
tree.create_node(44, "j", parent="e")
tree.create_node(47, "k", parent="e")
tree.create_node(52, "l", parent="f")
tree.create_node(54, "m", parent="f")
tree.create_node(59, "n", parent="g")
tree.create_node(68, "o", parent="g")

# Print the tree structure
tree.show()