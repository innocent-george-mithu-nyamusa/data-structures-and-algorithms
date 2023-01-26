from node import Node 

class DoublyLinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            
    def createDLL(self, nodeValue):
        node = Node(nodeValue)
        node.prev = None
        node.next = None
        self.head = node
        self.tail = node
        return "DLL created successfully created"
    
    def insertNode(self, nodeValue, location):
        if self.head is None:
            print("the node cannot be inserted")
        else:
            newNode = Node(nodeValue)
            if location == 0:
                newNode.prev = None
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode
            elif location == 1:
                newNode.next = None
                newNode.prev = self.tail
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location -1:
                    tempNode = tempNode.next
                    index += 1
                newNode.next = tempNode.next
                newNode.prev = tempNode
                newNode.next.prev = newNode 
                tempNode.next = newNode
                
                
    def traversal(self):
        if self.head is None:
            print("there is not linked list")
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next
                
    def reverseTraversal(self):
            if self.head is None:
                print("there is not linked list")
            else:
                tempNode = self.tail
                while tempNode:
                    print(tempNode.value)
                    tempNode = tempNode.prev
                    
    def searchDLL(self,nodeValue):
        if self.head is None:
            return "there i no node in List"
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == nodeValue:
                    return tempNode.value
                elif tempNode == self.tail:
                    return "The value does not exist in CDLL"
                tempNode = tempNode.next
                
dLL = DoublyLinkedList()
dLL.createDLL(2)

dLL.insertNode(2, 0)
dLL.insertNode(9, 1)
dLL.insertNode(22, 2)
dLL.insertNode(34, 2)
dLL.insertNode(90, 0)
dLL.insertNode(341, 2)

print([i.value for i in dLL])
dLL.searchDLL(2)
