#leetcode - 24
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

        while temp is not None:
            print(temp.value)
            temp = temp.next

    def swap_between(self):
        dummy = Node(0)
        dummy.next = self.head
        prev = dummy
        first = prev.next

        while first and  first.next :
            second = first.next
            #swap
            first.next = second.next 
            second.next = first
            prev.next = second
            #reassign to the next pair
            prev = first
            first = first.next

        #fixing head  
        self.head = dummy.next

        
    
my_ll = LinkedList(1)
my_ll.append(2)
my_ll.append(3)
my_ll.append(4)
my_ll.append(5)
my_ll.swap_between()
my_ll.print_list()
