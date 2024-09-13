from LinkedList.SinglyLinkedList import SinglyLinkedList


def fibonacciSequence(n):
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