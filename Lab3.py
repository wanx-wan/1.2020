class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

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
list.head = Node("Mon")
dt1 = Node("Tue")
dt2 = Node("Wed")
list.head.next = dt1
dt1.next = dt2
list.AtBg("Sun")
list.Atdt()
print()
print("addLast")
list.AtEnd("Thu")
list.new_data()
print()
print("insertAfter")
list.Inbt(list.head.next,"Fri")
list.new_data()