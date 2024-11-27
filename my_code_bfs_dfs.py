class BinaryTree:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key


def add_node(root, new_key):
    new_node = BinaryTree(new_key)

    if root == None:
        return new_node

    queue = []
    queue.append(root)

    while queue:
        temp = queue.pop(0)

        if temp.left:
            queue.append(temp.left)
        else:
            temp.left = new_node
            return root

        if temp.right:
            queue.append(temp.right)
        else:
            temp.right = new_node
            return root

    return root


def delete_node(root, value_delete):
    if root is None:
        return None

    if root.left is None and root.right is None:
        if root.key == value_delete:
            return None
        else:

            return root

    delete_node = None
    queue = []
    queue.append(root)

    while queue:
        temp = queue.pop(0)
        if temp.key == value_delete:
            delete_node = temp

        if temp.left:
            queue.append(temp.left)

        if temp.right:
            queue.append(temp.right)

    if delete_node:
        deepest_right_node = temp
        delete_node.key = deepest_right_node.key
        delete_deepest(root, deepest_right_node)

    return root


def delete_deepest(root, d_node):
    queue = []
    queue.append(root)

    while queue:
        temp = queue.pop(0)

        if temp == d_node:
            temp = None
            return

        if temp.left:
            if temp.left == d_node:
                temp.left = None
                return
            else:
                queue.append(temp.left)

        if temp.right:
            if temp.right == d_node:
                temp.right = None
                return
            else:
                queue.append(temp.right)


def bfs(root):

    if root is None:
        return

    result = []
    queue = []
    queue.append(root)

    while queue:
        temp = queue.pop(0)
        result.append(temp.key)

        if temp.left:
            queue.append(temp.left)

        if temp.right:
            queue.append(temp.right)
    return result


def dfs(node):
    if node is None:
        return []
    result = []
    result.append(node.key)

    if node.left:
        result.extend(dfs(node.left))

    if node.right:
        result.extend(dfs(node.right))
    return result


if __name__ == "__main__":
    A = BinaryTree(1)
    add_node(A, 2)
    add_node(A, 3)
    add_node(A, 4)
    add_node(A, 5)
    add_node(A, 6)
    add_node(A, 7)

    print(bfs(A))
    print(dfs(A))
