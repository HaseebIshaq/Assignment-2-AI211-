import turtle

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class TreeDrawer:
    def __init__(self, node_size=30, node_color='white', line_color='black'):
        self.node_size = node_size
        self.node_color = node_color
        self.line_color = line_color
        self.pen = turtle.Turtle()
        self.pen.speed('fastest')
        self.pen.hideturtle()
        self.pen.up()

    def draw_tree(self, root):
        self._draw_node(root, 0, 0)
        turtle.done()

    def _draw_node(self, node, x, y):
        if not node:
            return
        self.pen.goto(x, y)
        self.pen.down()
        self.pen.fillcolor(self.node_color)
        self.pen.begin_fill()
        self.pen.circle(self.node_size)
        self.pen.end_fill()
        self.pen.up()
        self.pen.goto(x, y - self.node_size - 10)
        self.pen.write(str(node.val), align='center', font=('Arial', 12, 'normal'))
        self.pen.goto(x, y - self.node_size)
        if node.left:
            self.pen.goto(x - 50, y - 50)
            self.pen.down()
            self.pen.pencolor(self.line_color)
            self.pen.goto(x - 100, y - 100)
            self.pen.up()
            self._draw_node(node.left, x - 100, y - 100)
        if node.right:
            self.pen.goto(x + 50, y - 50)
            self.pen.down()
            self.pen.pencolor(self.line_color)
            self.pen.goto(x + 100, y - 100)
            self.pen.up()
            self._draw_node(node.right, x + 100, y - 100)

# Example usage
root = TreeNode(50)
root.left = TreeNode(43)
root.right = TreeNode(55)
root.left.left = TreeNode(40)
root.left.right = TreeNode(45)
root.right.left = TreeNode(53)
root.right.right = TreeNode(60)
root.left.left.left = TreeNode(38)
root.left.left.right = TreeNode(41)
root.left.right.left = TreeNode(44)
root.left.right.right = TreeNode(47)
root.right.left.left = TreeNode(52)
root.right.left.right = TreeNode(54)
root.right.right.left = TreeNode(59)
root.right.right.right = TreeNode(68)

tree_drawer = TreeDrawer()
tree_drawer.draw_tree(root)
