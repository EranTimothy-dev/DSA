class SinglyLinkedList:
    def __init__(self, val, next=None):
        self.value = val
        self.next = next
    
    def __str__(self):
        return str(self.value)

        


if __name__ == "__main__":
    Head = SinglyLinkedList(1)
    A = SinglyLinkedList(2)
    B = SinglyLinkedList(3)
    C = SinglyLinkedList(4)
    Head.next = A
    A.next = B
    B.next = C
    # print(Head)

    # Traversing the list
    curr = Head
    while curr:
        print(curr)
        curr = curr.next

    # Search for a node
    def search(head, val):
        curr = head
        while curr:
            if val == curr.value:
                return True
            curr = curr.next
            
        return False


    print(search(Head, 3))