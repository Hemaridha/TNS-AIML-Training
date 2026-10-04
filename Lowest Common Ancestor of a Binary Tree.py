class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def lowest_common_ancestor(root, p, q):

    if root is None:
        return None

    if root == p or root == q:
        return root

    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)

    if left and right:
        return root

    if left:
        return left

    return right

root = TreeNode(3)

root.left = TreeNode(5)
root.right = TreeNode(1)

root.left.left = TreeNode(6)
root.left.right = TreeNode(2)

root.right.left = TreeNode(0)
root.right.right = TreeNode(8)

p = root.left       
q = root.right      

answer = lowest_common_ancestor(root, p, q)

print(answer.value)
