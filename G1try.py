class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.dt = None

class LinkedList:
    def __init__(self):
        self.head = None

    def Atdt(self):
        dt = self.head
        while dt is not None:
            print (dt.data)
            dt = dt.next

    def AtBg(self,newdata):
        New_Node = Node(newdata)
        New_Node.next = self.head
        self.head = New_Node

    def AtEnd(self, newdata):
        New_Node = Node(newdata)
        if self.head is None:
            self.head = New_Node
            return
        laste = self.head
        while(laste.next):
            laste = laste.next
        laste.next=New_Node

    def new_data(self):
        dt = self.head
        while dt is not None:
            print (dt.data)
            dt = dt.next
        
    def Deletedt(self, value):
        dt = self.head
        value = False
        if dt is None:
            value = False

    def Inbt(self,middle_node,newdata):
        if middle_node is None:
            print("The mentioned node is absent")
            return
        New_Node = Node(newdata)
        New_Node.next = middle_node.next
        middle_node.next = New_Node

    def new_data(self):
        dt = self.head
        while dt is not None:
            print (dt.data)
            dt = dt.next

list = LinkedList()
print("addFirst")
list.head = Node("10")
list.AtBg("20")
list.AtBg("30")
list.Atdt()
print()
print("insertAfter")
list.Inbt(list.head.next,"15")
list.new_data()
print()
print("Delete")
list.Deletedt("20")
print()
print("addLast")
list.AtEnd("40")
list.new_data()