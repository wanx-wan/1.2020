class Node:
  def __init__(self, dt, prevNode, nextNode):
    self.dt = dt
    self.prevNode = prevNode
    self.nextNode = nextNode
class DoubleLinkedList:
    def __init__(self, dt = None):
        self.head = None
        self.tail = None
        self.count = 0

    def addFirst(self, dt):
        if self.count == 0:
           self.head = Node(dt, None, None)
           self.tail = self.head
        elif self.count > 0:
            node = Node(dt, None, self.head)
            self.head.prevNode = node
            self.head = node
        self.current = self.head
        self.count += 1

    def insertAfter(self, prev_node, dt):
        current = self.head
        while current is not None:
                if current.dt == prev_node:
                   break
                current = current.nextNode 
        if current is None:
            return
        node = Node(dt, current, current.nextNode)
        current.nextNode = node
        if node.nextNode is not None:
            node.nextNode.prevNode = node

    def addLast(self, dt):
        if self.count == 0:
            self.addFirst(0)
        else:
            self.tail.nextNode = Node(dt, self.tail, None)
            self.tail = self.tail.nextNode
            self.count += 1

    def searchNode(self, value):    
        i = 1  
        flag = False       
        current = self.head    
                
        if self.head == None:    
            print("ไม่มี Node ที่ต้องการ")
            return    
                
        while current != None:        
            if current.dt == value:    
                flag = True  
                break   
            current = current.nextNode    
            i += 1  
                
        if flag:    
            print("Node " + str(i), "คือ ", value)    
        else:    
            print("ไม่มี Node ที่ต้องการ")

    def delete(self, value):
        current = self.head
        node_deleted = False
        if current is None:
            node_deleted = False

        elif current.dt == value:
            self.head = current.nextNode
            self.head.prevNode = None
            node_deleted = True

        elif self.tail.dt == value:
            self.tail = self.tail.prevNode
            self.tail.nextNode = None
            node_deleted = True

        else:
            while current:
                if current.dt == value:
                   current.prevNode.nextNode = current.nextNode
                   current.nextNode.prevNode = current.prevNode
                   node_deleted = True
                current = current.nextNode

        if node_deleted:
            self.count -= 1
        
    def traverse(self):
        curr = self.head
        while curr:
                print(curr.dt)
                curr = curr.nextNode
    
items = DoubleLinkedList()
items.addFirst("Python")
items.addFirst("Java")
items.addFirst("C++")
items.insertAfter("PHP","C")
print()
items.traverse()
items.delete("Java")
print()
items.traverse()
print()
items.searchNode("C++")