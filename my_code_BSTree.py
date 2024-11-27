class BinarySearchTree:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

    def add_node(self, key):
        return self._add_node(self, key)

    def _add_node(self, root, key):

        if root.key == key:
            return None

        if root.key > key:
            if root.left:
                self._add_node(root.left, key)
            else:
                root.left = BinarySearchTree(key)

        else:
            if root.right:
                self._add_node(root.right, key)
            else:
                root.right = BinarySearchTree(key)

    def search(self, key):
        return self._search(self, key)

    def _search(self, root, key):
        if root.key == key or root is None:
            return root

        if key < root.key:
            if root.left:
                return self._search(root.left, key)
            else:
                return None

        if root.right:
            return self._search(root.right, key)


def visualization(node):
    result = []
    result.append(node.key)
    if node.left:
        result.extend(visualization(node.left))
    if node.right:
        result.extend(visualization(node.right))

    return result


if __name__ == "__main__":
    root = BinarySearchTree(8)
    root.add_node(3)
    root.add_node(10)
    root.add_node(1)
    root.add_node(6)
    root.add_node(4)
    root.add_node(7)
    root.add_node(14)
    root.add_node(13)
    root.add_node(15)

    print(visualization(root))

    sample = [6, 9, 14, 16, 1, 2]
    for element in sample:
        result = root.search(element)
        if result:
            print('Exsist')
        else:
            print('Not exsist')
