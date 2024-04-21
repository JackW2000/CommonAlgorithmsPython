class Node:
    #   Function to initialise a Node object
    def __init__(self, data):
        self.data = data
        self.next_node = self.previous_node = None

    #   Function to get the data stored in a node
    def get_data(self):
        return self.data


class Queue:
    #   Function to initialise a queue object
    def __init__(self):
        #   Initialise head and tail as none
        self.head = self.tail = None

    #   Function to add an item to the end of a queue
    def enqueue(self, data):
        #   If the queue already contains data
        if self.tail is not None:
            #   Set the next_node for the tail to be a new node
            self.tail.next_node = Node(data)
            #   Set the previous node for the new node to be the current tail
            self.tail.next_node.previous_node = self.tail
            #   Update the tail to be the newly added node
            self.tail = self.tail.next_node
        else:
            #   Create a new node as the head
            self.head = Node(data)
            #   Set the tail to be the head
            self.tail = self.head

    #   Function to remove an item from the front of the queue
    def dequeue(self):
        #   Verify that the queue is not empty
        if self.head is not None:
            #   Store the node temporarily
            temp = self.head
            #   Update the head to point to the second node in the linked list (the next_node of current head)
            self.head = self.head.next_node
            #   Update previous node for the new node to be none as it is now the head
            self.head.previous_node = None
            #   Output that the node stored as temp has been dequeued
            print(str(temp.data) + " has been removed from the start of the queue.")
        else:
            #   The queue is empty so no data can be removed
            print("Sorry, the queue is currently empty!")

    #   Function to output all values in the queue in order
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

    #   Function to peek at the head of the queue
    def peek(self):
        #   Verify that there is data in the queue
        if self.head != self.tail:
            #
            print(str(self.head.data) + " is at the front of the queue.")
            return str(self.head.data) + " is at the front of the queue."
        else:
            #   The queue is empty so no data can be output
            print("Sorry, the queue is currently empty!")
            return "Sorry, the queue is currently empty!"

    #   Function to return the queue length
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

        #   Output the queue length
        print("The queue is " + str(node_count) + " nodes long.")
        return node_count

    #   Get the position of the head of the queue
    def get_head(self):
        return self.head

    #   Get the position of the tail of the queue
    def get_tail(self):
        return self.tail
