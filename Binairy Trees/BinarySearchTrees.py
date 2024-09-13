# In binary search trees the left subtree is always less than the root and the right subtree is always greater than the root
# Time: O(log(n)) | Space: O(log(n))
from DepthFirstSearch import TreeNode




# Check if Value exists (DFS) Time: O(log(n)), Space: O(log(n))
def search_bst(node, target):
    if not node:
        return False
    
    if node.val == target:
        return True
    
    if target < node.val:
        return search_bst(node.left, target)
    else:
        return search_bst(node.right, target)








if __name__ == "__main__":

    A = TreeNode(5)
    B = TreeNode(1)
    C = TreeNode(7)
    D = TreeNode(3)
    E = TreeNode(6)
    F = TreeNode(8)
    G = TreeNode(4)

    A.left = B
    A.right = C
    B.left = D
    B.right = E
    C.right = F
    C.left = G

    print(search_bst(A, 3))
    print(search_bst(A, 11))