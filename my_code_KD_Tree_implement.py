class BinaryTree:
    def __init__(self, point, left=None, right=None):
        self.left = left
        self.right = right
        self.point = point


def build_kd_tree(list_points, height=0):

    if not list_points:
        return None

    k = len(list_points[0])
    axis = height % k
    list_points.sort(key=lambda x: x[axis])
    median = len(list_points) // 2

    print("\naxis: ", axis)
    print("root_recursion: ", list_points[median])
    print('median: ', median)
    print('________________________')

    return BinaryTree(
        point=list_points[median],
        left=build_kd_tree(list_points[:median], height+1),
        right=build_kd_tree(list_points[median + 1:], height+1)
    )


my_list = [(1, 2), (2, 6), (3, 4), (5, 6), (7, 8), (8, 3)]
root = build_kd_tree(my_list)
