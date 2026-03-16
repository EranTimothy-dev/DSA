struct linkedListNode {
    int data;
    linkedListNode* next;

    linkedListNode(int value) : data(value), next(nullptr) {}

    void setNext(linkedListNode* nextNode) {
        next = nextNode;
    }
};

linkedListNode* head = nullptr;

int find(int value) {
    linkedListNode* current = head;
    while (current != nullptr) {
        if (current->data == value) {
            return current->data;
        } else {
            current = current->next;
        }
    }
    return -1;
}

int findRecursive(linkedListNode* current, int value) {
    // linkedListNode* current = head;
    if (current == nullptr) {
        return -1;
    } else if (current->data == value) {
        return current->data;
    } else {
        return findRecursive(current->next, value);
    }
}

void insert(int value) {
    if (head == nullptr) {
        head = new linkedListNode(value);
    } else {
        linkedListNode* current = head;
        while (current->next != nullptr) {
            current = current->next;
        }
        current->setNext(new linkedListNode(value));
    }
}
