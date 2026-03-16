#include <iostream>
#include <string>

using namespace std;

class BinarySeachTree {
    public:
        struct Node {
            int data;
            Node* left;
            Node* right;
            Node* parent;

            Node(int value) : data(value), left(nullptr), right(nullptr), parent(nullptr){}

            void setRightChild(Node* node) {
                right = node;
                if (node != nullptr) {
                    node->parent = this; // add parent reference to the child node for upward traversal
                }
            };

            void setLeftChild(Node* node) {
                left = node;
                if (node != nullptr) {
                    node->parent = this;
                }
            };
        };

    Node* root = nullptr;

    Node* find(int& value) {
        Node* current = root;
        while (current != nullptr) {
            if (value == current->data) {
                return current;
            } else if (value < current->data) {
                current =  current->left;
            } else {
                current = current->right;
            }
        }
        return nullptr;
    }

    void output(Node* node, string order) {
        if (order == "pre") {
            preOrderOutput(node);
        } else if (order == "in") {
            inOrderOutput(node);
        } else if (order == "post") {
            postOrderOutput(node);
        } else {
            cout << "Invalid order specified. Please use 'pre', 'in', or 'post'." << endl;
        }
    }

    void preOrderOutput(Node* node) {
        if (node == nullptr) {
            return;
        }
        cout << node->data << " ";
        preOrderOutput(node->left);
        preOrderOutput(node->right);
    }

    void inOrderOutput(Node* node) {
        if (node == nullptr) {
            return;
        }
        inOrderOutput(node->left);
        cout << node->data << " ";
        inOrderOutput(node->right);
    }

    void postOrderOutput(Node* node) {
        if (node == nullptr) {
            return;
        }
        postOrderOutput(node->left);
        postOrderOutput(node->right);
        cout << node->data << " ";
    }

    void insert(int value) {
    }

    void insertBelow(Node* node, int value) {
        if (node != nullptr) {
            if (value < node->data) {
                if (node->left == nullptr) {
                    node->setLeftChild(new Node(value));
                } else {
                    insertBelow(node->left, value);
                }
            } else {
                if (node->right == nullptr) {
                    node->setRightChild(new Node(value));
                } else {
                    insertBelow(node->right, value);
                }
            }
        }
    }

    void remove(int value) {
        Node* nodeToRemove = find(value);
        if (nodeToRemove == nullptr) {
            cout << "Value not found in the tree." << endl;
            return;
        }
        // case 1: node to remove has no children
        if (nodeToRemove->left == nullptr && nodeToRemove->right == nullptr) {
            if (nodeToRemove->parent == nullptr) {
                root = nullptr; // removing the root node
            } else if (nodeToRemove->parent->left == nodeToRemove) {
                nodeToRemove->parent->left = nullptr;
            } else {
                nodeToRemove->parent->right = nullptr;
            }
        }
        // case 2: node to remove has one child
        if (nodeToRemove->left != nullptr && nodeToRemove->right == nullptr) {
            if (nodeToRemove->parent == nullptr) { // where the node to remove is the root with a child
                root = nodeToRemove->left;
                root->parent = nullptr;
            } else if (nodeToRemove->parent->left == nodeToRemove) {
                nodeToRemove->parent->setLeftChild(nodeToRemove->left);
            } else {
                nodeToRemove->parent->setRightChild(nodeToRemove->left);
            }
        } else {
            if (nodeToRemove->parent == nullptr) {
                root = nodeToRemove->right;
                root->parent = nullptr;
            } else if (nodeToRemove->parent->left == nodeToRemove) {
                nodeToRemove->parent->setLeftChild(nodeToRemove->right);
            } else {
                nodeToRemove->parent->setRightChild(nodeToRemove->right);
            }
        }
    }

};
