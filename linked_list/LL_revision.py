#LL revision
"""
Topics covered
1. Creating Node
2. Creating LL
3. Printing LL
4. Empty LL
5. Append - last LL
6. Pop end
7. Pop first
8. Get
9. Insert
10. Remove

"""
#creating node

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self): #Prints LL
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def make_empty(self): #Empties LL
        self.head = None
        self.tail = None

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return



    def appened_last(self,value):
        new_node = Node(value)
        if self.length == 0: #First edge case having no head or tail
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    
    def pop_end(self):
        if self.length == 0: #First edge case if there are no items in the LL
            return None
        temp = self.head
        pre = self.head

        while (temp.next):
            pre = temp
            temp = temp.next 
        self.tail = pre
        self.temp.next = None
        self.length -=1
        if self.length == 0: #second edge case if there is only one item
            self.head = None
            self.tail = None
        return temp
    
    def pop_first(self):
        if self.length == 0: #First edge case the length of the LL is 0
            return None
        temp = self.head #Second edge case the length is 2 or more than 2
        self.head = self.head.next
        temp.next = None
        self.length -=1 #Third edge case the lenght is 1
        if self.length == 0:
            self.tail = None

    def get(self, index): #gets the node at a specific Index
        if index < 0 or index > self.length: #Checks the length of the LL, is greater than 0 and less than the max length.
            return None #If it is then return 0
        
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    def set (self,index,value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True 
        return False
    
    def insert(self,index,value):
        if index > self.length or index < 0:
            return None
        if self.length == 0:
            return self.prepend(value) 
        if index ==  self.length:
            return self.appened_last(value)
        new_node = Node(value)
        temp = self.get(index -1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True
    def remove(self, index):
        if index < 0 or index > self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length -1 :
            return self.pop_end
        prev = self.get(index -1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp

        after = temp.next
        before = None

        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
    

        
my_linkedlist = LinkedList(5)
my_linkedlist.appened_last(4)
my_linkedlist.appened_last(3)
my_linkedlist.appened_last(2)
my_linkedlist.appened_last(1)
my_linkedlist.reverse()
my_linkedlist.print_list()



