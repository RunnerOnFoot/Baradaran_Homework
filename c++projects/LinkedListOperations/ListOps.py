class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_node(self, data, position):
        new_node = Node(data)
        
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        
        temp = self.head
        for _ in range(position - 1):
            if temp is None:
                print("Position is out of bounds")
                return
            temp = temp.next
        
        if temp is None:
            print("Position is out of bounds")
            return
        
        new_node.next = temp.next
        temp.next = new_node

    def delete_node(self, data):
        temp = self.head
        prev = None

        if temp is not None and temp.data == data:
            self.head = temp.next
            return

        while temp is not None and temp.data != data:
            prev = temp
            temp = temp.next

        if temp is None:
            print(f"Node with data {data} not found")
            return

        prev.next = temp.next

    def delete_list(self):
        self.head = None

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("NULL")

if __name__ == "__main__":
    list = LinkedList()
    
    list.insert_node(10, 0)
    list.insert_node(20, 1)
    list.insert_node(30, 2)
    list.insert_node(15, 1)
    
    print("Linked list after insertions:")
    list.print_list()
    
    list.delete_node(20)
    print("Linked list after deleting node with data 20:")
    list.print_list()
    
    list.delete_list()
    print("Linked list after deleting the entire list:")
    list.print_list()
