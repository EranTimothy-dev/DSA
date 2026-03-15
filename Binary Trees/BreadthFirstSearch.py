from collections import deque
from DepthFirstSearch import TreeNode

# Level Order Traversal (BFS) Time: O(n), Space: O(n)
def level_order(node):
    q = deque()
    q.append(node)

    while q:
        node = q.popleft()
        print(node)
        # since BFS are queues which are FIFO, so first the left and then the right
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    



if __name__ == "__main__":
    
    A = TreeNode(1)
    B = TreeNode(2)
    C = TreeNode(3)
    D = TreeNode(4)
    E = TreeNode(5)

    A.left = B
    A.right = C
    B.left = D
    B.right = E

    level_order(A)












