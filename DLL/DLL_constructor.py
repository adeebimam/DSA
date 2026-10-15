#Creating construct of DLL

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None #Compared to a LL, there is another attribute prev which point the prev node


class Doubly_Linked_List:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.tail = new_node

    def print_list(self):
        temp = self.head

        while temp:
            print(temp.value)
            temp = temp.next


my_dLL = Doubly_Linked_List(7)

my_dLL.print_list()

