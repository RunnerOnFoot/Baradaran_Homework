#include <iostream>

// Node structure
struct Node
{
    int data;
    Node *next;

    Node(int value) : data(value), next(nullptr) {}
};

// Linked List class
class LinkedList
{
private:
    Node *head;

public:
    LinkedList() : head(nullptr) {}

    // Function to insert a node at a specific position
    void insertNode(int data, int position)
    {
        Node *newNode = new Node(data);

        if (position == 0)
        {
            newNode->next = head;
            head = newNode;
            return;
        }

        Node *temp = head;
        for (int i = 0; temp != nullptr && i < position - 1; ++i)
        {
            temp = temp->next;
        }

        if (temp == nullptr)
        {
            std::cout << "Position is out of bounds" << std::endl;
            delete newNode;
            return;
        }

        newNode->next = temp->next;
        temp->next = newNode;
    }

    // Function to delete a node with a specific value
    void deleteNode(int data)
    {
        Node *temp = head;
        Node *prev = nullptr;

        if (temp != nullptr && temp->data == data)
        {
            head = temp->next;
            delete temp;
            return;
        }

        while (temp != nullptr && temp->data != data)
        {
            prev = temp;
            temp = temp->next;
        }

        if (temp == nullptr)
        {
            std::cout << "Node with data " << data << " not found" << std::endl;
            return;
        }

        prev->next = temp->next;
        delete temp;
    }

    // Function to delete the entire linked list
    void deleteList()
    {
        Node *current = head;
        Node *next = nullptr;

        while (current != nullptr)
        {
            next = current->next;
            delete current;
            current = next;
        }

        head = nullptr;
    }

    // Function to print the linked list
    void printList() const
    {
        Node *temp = head;
        while (temp != nullptr)
        {
            std::cout << temp->data << " -> ";
            temp = temp->next;
        }
        std::cout << "NULL" << std::endl;
    }

    // Destructor to clean up the memory
    ~LinkedList()
    {
        deleteList();
    }
};

int main()
{
    LinkedList list;

    list.insertNode(10, 0);
    list.insertNode(20, 1);
    list.insertNode(30, 2);
    list.insertNode(15, 1);

    std::cout << "Linked list after insertions: ";
    list.printList();

    list.deleteNode(20);
    std::cout << "Linked list after deleting node with data 20: ";
    list.printList();

    list.deleteList();
    std::cout << "Linked list after deleting the entire list: ";
    list.printList();

    return 0;
}
