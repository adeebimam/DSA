#leetcode 1290
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp =self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    
    def binary_to_decimal(self):
        current = self.head
        decimal = 0

        while current:
            decimal = decimal*2 + current.value
            current = current.next
        return decimal


my_ll = LinkedList(1)
my_ll.append(0)
my_ll.append(1)
my_ll.append(1)

print(my_ll.binary_to_decimal())
