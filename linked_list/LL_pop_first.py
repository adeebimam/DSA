#In popppoing the first item of LL there are 3 scenarios

#1 Zero items in the LL
#2 Two or more items in the LL
#3 One item in the LL

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
        temp = self.head
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
    
    def pop_first(self):
        if self.length == 0:
            return None
        else:
            temp = self.head 
            self.head = self.head.next
            temp.next = None
            self.length -= 1
            if self.length == 0:
                self.tail.next = None
        return temp.value

my_LL = LinkedList(2)
my_LL.append(1)
print(my_LL.pop_first())
print(my_LL.pop_first())
print(my_LL.pop_first())