#leetcode 92
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
    
    def append(self,value):
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    
    def print_list(self):
        temp = self.head 

        while temp:
            print(temp.value)
            temp = temp.next
    
    def reverse_between(self, left, right):
        current = self.head

        dummy = Node(0)
        dummy.next = self.head

        prev = dummy

        for _ in range(left - 1):
            prev = prev.next

        current = prev.next

        for _ in range (right - left):
            temp = current.next 
            current.next = temp.next
            temp.next = prev.next
            prev.next = temp
            self.head = dummy.next

        if right == self.length:
            self.tail = current
        return self.head
        
my_ll = LinkedList(1)

my_ll.append(2)
my_ll.append(3)
my_ll.append(4)
my_ll.append(5)
my_ll.reverse_between(2,4)

my_ll.print_list()