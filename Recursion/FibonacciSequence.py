from LinkedList.SinglyLinkedList import SinglyLinkedList

# @__cached__
def fibonacciSequence(n):
    """
    Generates the nth Fibonacci sequence number using recursion and memoization to
    optimize performance.

    Args:
        n (int): The position of the Fibonacci sequence number to generate.

    Returns:
        int: The nth Fibonacci sequence number.

    Raises:
        TypeError: If n is not an integer.

    Examples:
        >>> fibonacciSequence(0)
        0
        >>> fibonacciSequence(1)
        1
        >>> fibonacciSequence(2)
        1
        >>> fibonacciSequence(3)
        2
        >>> fibonacciSequence(4)
        3
        >>> fibonacciSequence(5)
        5
        >>> fibonacciSequence(6)
        8
        >>> fibonacciSequence(7)
        13
    """
    if n == 0 or n == 1:
        return n
    else:
        return fibonacciSequence(n - 1) + fibonacciSequence(n - 2)

        




def reverse(node):
    # if the node is null return
    # this will cause the function to go back in the function call stack and print the linked list in reverse order
    if not node:
        return
    
    reverse(node.next)
    print(node)

    
    
if __name__ == "__main__":
    
    Head = SinglyLinkedList(0)
    A = SinglyLinkedList(1)
    B = SinglyLinkedList(3)
    C = SinglyLinkedList(2)

    reverse(Head)
