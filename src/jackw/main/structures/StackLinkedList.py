class Node:
    #   Function to initialise a Node object
    def __init__(self, data):
        self.data = data
        self.next_node = self.previous_node = None

    #   Function to get the data of the node
    def get_data(self):
        return self.data


class Stack:
    #   Function to initialise a stack object
    def __init__(self):
        #   Initialise head as none
        self.head = None

    #   Function to add an item to the top of a stack
    def push(self, data):
        #   If the stack already contains data
        if self.head is not None:
            #   Create the new head node
            temp = Node(data)
            #   Set the next node for the new node to be the current head node
            temp.next_node = self.head
            #   Set the previous_node for the current head to be the new node
            self.head.previous_node = temp
            #   Update the head to be the new node
            self.head = temp
        else:
            #   Create a new node as the head
            self.head = Node(data)
        return str(data) + " has been successfully added to the top stack."

    #   Function to remove an item from the top of the stack
    def pop(self):
        #   Verify that the stack is not empty
        if self.head is not None:
            #   Store the node temporarily
            temp = self.head
            #   Update the head to point to the second node in the linked list (the next_node of current head)
            self.head = self.head.next_node
            #   Update previous node for the new node to be none as it is now the head
            self.head.previous_node = None
            #   Output that the node stored as temp has been dequeued
            response = str(temp.data) + " has been removed from the top of the stack."
        else:
            #   The stack is empty so no data can be removed
            response = "Sorry, the stack is currently empty!"
        return response

    #   Function to output all values in the stack in order
    def display(self):
        response = ""
        #   Initialise counter
        position = 0
        #   Store head node as temp
        temp = self.head
        #   Loop until there are no nodes left
        while temp is not None:
            #   Output the position (counter) and the data of the node
            response += "Position " + str(position) + " holds " + str(temp.data) + "\n"
            #   Update temp to point to the next node
            temp = temp.next_node
            #   Increment counter
            position += 1
        print(response)
        return response

    #   Function to peek at the head of the stack
    def peek(self):
        #   Verify that there is data in the stack
        if self.head is not None:
            #
            response = str(self.head.data) + " is on top of the stack."
        else:
            #   The stack is empty so no data can be output
            response = "Sorry, the stack is currently empty!"
        return response

    #   Function to return the stack length
    def get_length(self):
        #   Store head node as temp
        temp = self.head
        #   Initialise counter
        node_count = 0
        #   Loop until there are no nodes left
        while temp is not None:
            #   Update temp to point to the next node
            temp = temp.next_node
            #   Increment counter
            node_count += 1

        #   Output the stack length
        print("The stack is " + str(node_count) + " nodes long.")
        return "The stack is " + str(node_count) + " nodes long."
