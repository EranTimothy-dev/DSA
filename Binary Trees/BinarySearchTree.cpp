#include <iostream>

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

};
