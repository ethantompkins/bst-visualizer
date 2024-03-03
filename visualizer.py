import graphviz

def visualize_tree(tree, root):
    dot = graphviz.Digraph()
    dot.node(str(root.data))
    tree.add_edge(root, dot)
    dot.render("tree", format="png")