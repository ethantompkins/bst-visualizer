class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None
        self.nodes = ""

    def add_node(self, data):
        currnode = Node(data)
        if self.root is None:
            self.root = currnode
        else:
            parent = None
            ptr = self.root
            while ptr is not None:
                parent = ptr
                if int(currnode.data) < int(ptr.data):
                    ptr = ptr.left
                else:
                    ptr = ptr.right
            if int(currnode.data) < int(parent.data):
                parent.left = currnode
            else:
                parent.right = currnode

    def inorder(self, root):
        if root != None:
            self.inorder(root.left)
            self.nodes += root.data + " "
            self.inorder(root.right)

    def preorder(self, root):
        if root != None:
            self.nodes += root.data + " "
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root != None:
            self.postorder(root.left)
            self.postorder(root.right)
            self.nodes += root.data + " "

    def visualize_tree(self, root):
        dot = graphviz.Digraph()
        dot.node(str(root.data))
        self.addedge(root,dot)
        dot.render("tree",format="png")

    def add_edge(self, node, dot):
        if node.left:
            dot.node(str(node.left.data))
            dot.edge(str(node.data),str(node.left.data))
            self.addedge(node.left,dot)
        if node.right:
            dot.node(str(node.right.data))
            dot.edge(str(node.data),str(node.right.data))
            self.addedge(node.right,dot)