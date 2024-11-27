from graphviz import Graph

class BinaryTree:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.value = data


def add_node(root, data):
    
    new_node = BinaryTree(data)
    if root == None:
        return new_node

    binary_queue = []
    binary_queue.append(root)

    while binary_queue:
        node = binary_queue.pop(0)

        if node.left:
            binary_queue.append(node.left)
        else:
            node.left = new_node
            return root

        if node.right:
            binary_queue.append(node.right)
        else:
            node.right = new_node
            return root

    return root


def add_edges(dot, node):

    if node is None:
        return

    if node.left:
        dot.edge(str(node.value), str(node.left.value))
        add_edges(dot, node.left)

    if node.right:
        dot.edge(str(node.value), str(node.right.value))
        add_edges(dot, node.right)


def visualization(root):
    dot = Graph()
    dot.node(str(root.value))

    add_edges(dot, root)
    return dot


if __name__ == "__main__":

    A = BinaryTree("A")
    A.left = BinaryTree("B")
    A.right = BinaryTree("C")
    A.left.left = BinaryTree("D")
    A.right.right = BinaryTree("E")

    new_data = "F"
    A = add_node(A, new_data)

    dot = visualization(A)
    dot.render('tree', format='png', view=True)
