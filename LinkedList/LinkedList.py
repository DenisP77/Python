
# class node:
#     def __init__(self, data=None):
#         self.data = data
#         self.next = None
#
# class linked_list:
#     def __init__(self):
#         self.head = node()
#
#     def append(self, data):
#         new_node = node(data)
#         cur = self.head
#         while cur.next != None:
#             cur = cur.next
#         cur.next = new_node
#
#     def length(self):
#         cur = self.head
#         total = 0
#         while cur.next != None:
#             total += 1
#             cur = cur.next

# Node class
class Node:
    def __init__(self, data):
        self.data = data  # Stores the data
        self.next = None  # Points to the next node

    def __repr__(self):
        # Memory address of the current node (self)
        current_node_address = hex(id(self))

        # Memory address of the next node (self.next)
        if self.next:
            next_node_address = hex(id(self.next))
        else:
            next_node_address = 'None'

        # Custom string representation
        return f"Node object at address {current_node_address} -> Data: {self.data}, Next: {next_node_address}"



# Linked List class
class LinkedList:
    def __init__(self):
        self.head = None  # Head of the linked list (first node)

    # Insert a new node at the end
    def append(self, data):
        new_node = Node(data)

        # If the list is empty, make the new node the head
        if self.head is None:
            self.head = new_node
            return

        # Otherwise, traverse to the last node
        last_node = self.head
        while last_node.next:
            last_node = last_node.next

        # Make the last node point to the new node
        last_node.next = new_node

    # Print the linked list
    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")  # Indicates the end of the list

    def print_with_addresses(self):
        current = self.head
        while current:
            print(f"Data: {current.data}, Address: {id(current)}")
            current = current.next
        print("End of List")

    # Display the entire linked list
    def display(self):
        current = self.head
        while current:
            print(current)  # This will call __repr__() for each node
            current = current.next
        print("End of List")

    # Delete a node by its value
    def delete_node(self, key):
        current_node = self.head

        # If the node to be deleted is the head
        if current_node and current_node.data == key:
            self.head = current_node.next
            current_node = None
            return

        # Otherwise, find the node to delete
        prev_node = None
        while current_node and current_node.data != key:
            prev_node = current_node
            current_node = current_node.next

        # If the node was not found
        if current_node is None:
            print("Node not found")
            return

        # Unlink the node from the list
        prev_node.next = current_node.next
        current_node = None


# # Example
# ll = LinkedList()
# ll.append(10)
# Node object at address 0x1a2b3c  ->  Data: 10, Next: None
# ll.append(20)
# ll.append(30)
# head -> Node(data=10, next=Node(data=20, next=Node(data=30, next=None)))

