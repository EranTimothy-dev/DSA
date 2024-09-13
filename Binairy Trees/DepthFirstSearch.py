# DFS is generally stacks or recursion
# BFS is generally queues

class  TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
    def __str__(self):
        return str(self.val)



# Recursion Pre Order Traversal (DFS) Time: O(n), Space: O(n)
def pre_order(node):
    if not node:
        return
    
    print(node)
    pre_order(node.left)
    pre_order(node.right)

# Recursion In Order Traversal (DFS) Time: O(n), Space: O(n)
def in_order(node):
    if not node:
        return
    
    in_order(node.left)
    print(node)
    in_order(node.right)
    
# Recursion Post Order Traversal (DFS) Time: O(n), Space: O(n)
def post_order(node):
    if not node:
        return
    
    post_order(node.left)
    post_order(node.right)
    print(node)


# Iterative Pre Order Traversal (DFS) Time: O(n), Space: O(n)
def pre_order_iterative(node):
    stack = [node]
    
    # while the stack is not empty
    while stack:
        node = stack.pop()
        print(node)
        # since its a stack first the right and then the left
        # because stacks are LIFO so then the left will be processed before right
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
        
# the position of the print statement does not have an effect in the iterative approach
def pre_order_iterative2(node):
    stack = [node]
    
    # while the stack is not empty
    while stack:
        node = stack.pop()
        if node.right:
            stack.append(node.right)
        print(node)
        if node.left:
            stack.append(node.left)


# Check if Value exists (DFS) Time: O(n), Space: O(n)
def search(node, target):
    if not node:
        return False
    if node.val == target:
        return True
    
    return search(node.left, target) or search (node.right, target)







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

    # pre_order_iterative(A)
    # print("\n")
    # pre_order_iterative2(A)
    print(search(A, 3))
    print(search(A, 11))